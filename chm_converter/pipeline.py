import asyncio
import gc
import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Optional

import aiofiles

from .config import ConversionConfig, DEFAULT_CONFIG
from .encoding import read_file_with_encoding
from .extractor import export_chm_to_htm, find_html_folder
from .image_processor import ImageStore
from .indexer import build_file_dictionary, create_index_files, _collect_html_files
from .md_converter import convert_html_to_markdown


# ---------------------------------------------------------------------------
# Single-file conversion
# ---------------------------------------------------------------------------

async def _process_file(
    executor: ThreadPoolExecutor,
    input_path: str,
    output_path: str,
    semaphore: asyncio.Semaphore,
    file_dictionary: Dict,
    version: Optional[str],
    cfg: ConversionConfig,
    preserve_structure: bool,
    image_store: Optional[ImageStore],
) -> None:
    loop = asyncio.get_running_loop()
    try:
        async with semaphore:
            html = await read_file_with_encoding(input_path)
        markdown = await loop.run_in_executor(
            executor,
            convert_html_to_markdown,
            html,
            file_dictionary,
            version,
            cfg,
            preserve_structure,
            image_store,
            input_path,
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        async with semaphore:
            async with aiofiles.open(output_path, "w", encoding="utf-8") as f:
                await f.write(markdown)
    except Exception as exc:
        print(f"Error converting {input_path}: {exc}")


# ---------------------------------------------------------------------------
# Batch conversion
# ---------------------------------------------------------------------------

async def _convert_files(
    input_folder: str,
    data_folder: str,
    core_folder: str,
    file_dictionary: Dict,
    version: Optional[str],
    cfg: ConversionConfig,
    max_workers: int,
    semaphore_limit: int,
    batch_size: int,
    preserve_structure: bool,
    image_store: Optional[ImageStore],
) -> None:
    html_folder = find_html_folder(input_folder)
    if not html_folder:
        print(f"No HTML files found in: {input_folder}")
        return

    os.makedirs(data_folder, exist_ok=True)
    os.makedirs(core_folder, exist_ok=True)

    # Collect all HTML files recursively (fixes issue #10 — nested structures)
    rel_paths = _collect_html_files(html_folder)
    total = len(rel_paths)
    print(f"Converting {total} HTML files to Markdown...")

    semaphore = asyncio.Semaphore(semaphore_limit)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(0, total, batch_size):
            batch = rel_paths[i: i + batch_size]
            tasks = []
            for rel in batch:
                abs_input = os.path.join(html_folder, rel)

                if preserve_structure:
                    out_rel = os.path.splitext(rel)[0] + ".md"
                else:
                    out_rel = os.path.splitext(os.path.basename(rel))[0] + ".md"

                output_path = os.path.join(data_folder, out_rel)
                tasks.append(
                    _process_file(
                        executor,
                        abs_input,
                        output_path,
                        semaphore,
                        file_dictionary,
                        version,
                        cfg,
                        preserve_structure,
                        image_store,
                    )
                )
            await asyncio.gather(*tasks)
            batch_no = i // batch_size + 1
            remaining = total - min(i + batch_size, total)
            print(f"Batch {batch_no}: {len(batch)} files converted. {remaining} remaining.")
            if batch_no % 50 == 0:
                gc.collect()

    await create_index_files(core_folder, file_dictionary, version)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def process_chm_file(
    chm_file_path: str,
    base_input_folder: str,
    base_output_folder: str,
    cfg: ConversionConfig = DEFAULT_CONFIG,
    max_workers: int = 4,
    semaphore_limit: int = 20,
    batch_size: int = 10,
    keep_html: bool = False,
    preserve_structure: bool = False,
) -> bool:
    """Extract *chm_file_path*, convert to Markdown, write to *base_output_folder*.

    Args:
        keep_html:          Retain the extracted HTML tree after conversion.
        preserve_structure: Mirror the CHM's internal folder hierarchy in the
                            output ``data/`` directory.  Default is flat output.

    Returns *True* on success.
    """
    version = os.path.splitext(os.path.basename(chm_file_path))[0]
    print(f"\n=== Processing {version} ===")

    input_folder = os.path.join(base_input_folder, version)
    output_folder = os.path.join(base_output_folder, version)
    data_folder = os.path.join(output_folder, "data")
    core_folder = os.path.join(output_folder, "core")
    images_folder = os.path.join(output_folder, "images")

    for folder in (input_folder, output_folder, data_folder, core_folder, images_folder):
        os.makedirs(folder, exist_ok=True)

    print(f"Extracting {chm_file_path} -> {input_folder}")
    if not await export_chm_to_htm(chm_file_path, input_folder):
        print(f"Extraction failed for {chm_file_path}. Skipping.")
        return False

    image_store = ImageStore(images_folder)

    file_dictionary = await build_file_dictionary(
        input_folder, version, preserve_structure
    )
    await _convert_files(
        input_folder,
        data_folder,
        core_folder,
        file_dictionary,
        version,
        cfg,
        max_workers,
        semaphore_limit,
        batch_size,
        preserve_structure,
        image_store,
    )

    if not keep_html:
        # Remove entire extraction folder — output is written to base_output_folder
        shutil.rmtree(input_folder, ignore_errors=True)

    print(f"=== Completed {version} ===")
    return True


async def process_all_chm_files(
    resources_folder: str,
    base_input_folder: str,
    base_output_folder: str,
    cfg: ConversionConfig = DEFAULT_CONFIG,
    max_workers: int = 8,
    semaphore_limit: int = 20,
    batch_size: int = 50,
    keep_html: bool = False,
    preserve_structure: bool = False,
) -> None:
    """Process every CHM file found in *resources_folder*."""
    chm_files = [
        os.path.join(resources_folder, f)
        for f in os.listdir(resources_folder)
        if f.lower().endswith(".chm")
    ]
    if not chm_files:
        print(f"No CHM files found in {resources_folder}.")
        return

    print(f"Found {len(chm_files)} CHM file(s) to process.")
    results = []
    for chm_file in chm_files:
        ok = await process_chm_file(
            chm_file,
            base_input_folder,
            base_output_folder,
            cfg,
            max_workers,
            semaphore_limit,
            batch_size,
            keep_html,
            preserve_structure,
        )
        results.append((chm_file, ok))

    success = sum(1 for _, ok in results if ok)
    print(f"\n=== Summary: {success}/{len(chm_files)} succeeded ===")
    for chm_file, ok in results:
        if not ok:
            print(f"  FAILED: {os.path.basename(chm_file)}")
