import asyncio
import gc
import json
import os
from typing import Dict, Optional

import aiofiles
from bs4 import BeautifulSoup

from .encoding import read_file_with_encoding
from .extractor import find_html_folder
from .html_processor import extract_keywords, extract_page_title


def _collect_html_files(html_folder: str) -> list[str]:
    """Return relative paths of all HTML files under *html_folder* (recursive)."""
    found = []
    for root, _, files in os.walk(html_folder):
        for name in files:
            if name.lower().endswith((".htm", ".html")):
                rel = os.path.relpath(os.path.join(root, name), html_folder)
                found.append(rel.replace("\\", "/"))  # normalise to forward slashes
    return found


async def build_file_dictionary(
    input_folder: str,
    version: Optional[str] = None,
    preserve_structure: bool = False,
    batch_size: int = 100,
) -> Dict:
    """Scan all HTML files in *input_folder* (recursively) and build a title map.

    Dictionary keys are:
      - ``preserve_structure=False``: bare filename stem (e.g. ``"MyClass"``)
      - ``preserve_structure=True``:  relative path stem  (e.g. ``"api/MyClass"``)

    Processing is batched to keep memory usage bounded on large CHM files.
    """
    html_folder = find_html_folder(input_folder)
    if not html_folder:
        print(f"No HTML files found in: {input_folder}")
        return {}

    file_list = _collect_html_files(html_folder)
    print(f"Building dictionary from {len(file_list)} HTML files...")

    semaphore = asyncio.Semaphore(20)
    file_dictionary: Dict = {}

    async def _process(rel_path: str):
        abs_path = os.path.join(html_folder, rel_path)
        if preserve_structure:
            key = os.path.splitext(rel_path)[0]          # e.g. "api/MyClass"
        else:
            key = os.path.splitext(os.path.basename(rel_path))[0]  # e.g. "MyClass"
        try:
            async with semaphore:
                html = await read_file_with_encoding(abs_path)
            soup = BeautifulSoup(html, "html.parser")
            title = extract_page_title(soup) or "Untitled Document"
        except Exception as exc:
            print(f"Error reading {abs_path} for dictionary: {exc}")
            title = "Error Document"
        entry = {"title": title, "filename": key + ".md"}
        if version:
            entry["version"] = version
        return key, entry

    for i in range(0, len(file_list), batch_size):
        batch = file_list[i: i + batch_size]
        results = await asyncio.gather(*[_process(f) for f in batch])
        for key, info in results:
            file_dictionary[key] = info
        if (i // batch_size + 1) % 10 == 0:
            gc.collect()

    print(f"Dictionary built: {len(file_dictionary)} entries")
    return file_dictionary


async def create_index_files(
    core_folder: str,
    file_dictionary: Dict,
    version: Optional[str] = None,
) -> None:
    """Write ``file_index.json``, ``id_lookup.json``, and ``index.md`` into *core_folder*."""

    # file_index.json — raw mapping
    index_path = os.path.join(core_folder, "file_index.json")
    async with aiofiles.open(index_path, "w", encoding="utf-8") as f:
        await f.write(json.dumps(file_dictionary, indent=4, ensure_ascii=False))
    print(f"Created file index: {index_path}")

    # id_lookup.json — lowercase keys + extracted keywords
    id_lookup: Dict = {}
    for file_id, info in file_dictionary.items():
        entry = {
            "title": info["title"],
            "filename": info["filename"],
            "keywords": extract_keywords(info["title"]),
        }
        v = version or info.get("version")
        if v:
            entry["version"] = v
        id_lookup[file_id.lower()] = entry

    lookup_path = os.path.join(core_folder, "id_lookup.json")
    async with aiofiles.open(lookup_path, "w", encoding="utf-8") as f:
        await f.write(json.dumps(id_lookup, indent=4, ensure_ascii=False))
    print(f"Created ID lookup: {lookup_path}")

    # index.md — alphabetical navigation
    md_path = os.path.join(core_folder, "index.md")
    sorted_entries = sorted(
        file_dictionary.items(),
        key=lambda x: x[1]["title"].lower(),
    )
    async with aiofiles.open(md_path, "w", encoding="utf-8") as f:
        heading = f"# Documentation Index — Version {version}" if version else "# Documentation Index"
        await f.write(heading + "\n\n")

        first_letters = sorted(
            {e[1]["title"][0].upper() for e in sorted_entries if e[1]["title"]}
        )
        await f.write("## Quick Navigation\n\n")
        await f.write(" | ".join(f"[{lt}](#{lt.lower()})" for lt in first_letters))
        await f.write("\n\n")

        current_letter = None
        for _, info in sorted_entries:
            title = info["title"]
            if not title:
                continue
            letter = title[0].upper()
            if letter != current_letter:
                current_letter = letter
                await f.write(f"\n## {letter}\n<a id='{letter.lower()}'></a>\n\n")
            await f.write(f"- [{title}](../data/{info['filename']})\n")

    print(f"Created index: {md_path}")
