import os
from pathlib import Path
import re
from typing import Dict, Optional, Tuple

from bs4 import BeautifulSoup

from .config import ConversionConfig
from .image_processor import ImageStore


def extract_page_title(soup: BeautifulSoup) -> Optional[str]:
    """Return the best available page title from *soup*, or *None*."""
    tag = soup.find("title")
    if tag and tag.string:
        return tag.string.strip()
    for level in range(1, 7):
        heading = soup.find(f"h{level}")
        if heading:
            text = heading.get_text(strip=True)
            if text:
                return text
    return None


def extract_keywords(title: Optional[str]) -> list:
    """Return a list of significant words from *title* for search indexing."""
    if not title:
        return []
    stopwords = {
        "a", "an", "the", "and", "or", "of", "to", "in",
        "for", "with", "on", "at", "by", "is", "are", "was", "were",
    }
    words = re.findall(r"\b\w+\b", title.lower())
    keywords = [w for w in words if w not in stopwords and len(w) > 2]
    if title.lower() not in keywords:
        keywords.append(title.lower())
    return keywords


def remove_unwanted_elements(soup: BeautifulSoup, cfg: ConversionConfig) -> BeautifulSoup:
    """Strip tags, classes, IDs, and junk links defined in *cfg*."""
    for tag_name in cfg.tags_to_remove:
        for el in soup.find_all(tag_name):
            el.decompose()

    if cfg.classes_to_remove:
        for el in soup.find_all(
            lambda t: t.has_attr("class")
            and any(c in t.get("class") for c in cfg.classes_to_remove)
        ):
            el.decompose()

    for elem_id in cfg.ids_to_remove:
        for el in soup.find_all(id=elem_id):
            el.decompose()

    # Remove javascript: and mailto: links universally
    for a in soup.find_all("a", href=lambda h: h and "javascript:" in str(h).lower()):
        a.decompose()
    for a in soup.find_all("a", href=lambda h: h and "mailto:" in str(h).lower()):
        a.decompose()

    return soup


def update_links(
    soup: BeautifulSoup,
    file_dictionary: Optional[Dict] = None,
    preserve_structure: bool = False,
) -> BeautifulSoup:
    """Rewrite .htm/.html hrefs to .md and optionally annotate with titles.

    When *preserve_structure* is False (default), the directory part of each
    href is stripped so that all links point to flat filenames — matching the
    flat ``data/`` output layout.

    When *preserve_structure* is True, only the extension is changed so that
    relative subdirectory paths are preserved — matching the nested output layout.
    """
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href == "#PageHeader":
            a.decompose()
            continue
        if href.lower().endswith((".htm", ".html")):
            if preserve_structure:
                # Keep relative path; normalise separators for Markdown
                rel = os.path.splitext(href.replace("\\", "/"))[0]
                a["href"] = rel + ".md"
                # Try full relative key first, then basename fallback
                key = rel
                if file_dictionary and key not in file_dictionary:
                    key = os.path.basename(rel)
            else:
                key = os.path.splitext(os.path.basename(href))[0]
                a["href"] = key + ".md"

            if file_dictionary and key in file_dictionary:
                display = file_dictionary[key].get("title")
                if display:
                    a["title"] = display
    return soup


def update_images(
    soup: BeautifulSoup,
    image_store: Optional[ImageStore],
    html_file_path: Optional[str] = None,
    markdown_output_path: Optional[str] = None,
) -> BeautifulSoup:
    """Materialize images referenced by ``<img>`` tags into *image_store*.

    Successfully processed images have their ``src`` rewritten to point at
    the local ``images/<md5>.<ext>`` file using a path relative to the
    Markdown output file. Failures leave the original ``src`` untouched so
    the reference is preserved whenever possible.
    """
    if image_store is None:
        return soup

    for img in soup.find_all("img", src=True):
        src = img["src"]
        try:
            filename = image_store.process(src, html_file_path)
        except Exception as exc:
            print(f"Error processing image '{src}': {exc}")
            filename = None
        if filename:
            if markdown_output_path:
                image_path = Path(image_store.images_folder) / filename
                relative_path = os.path.relpath(image_path, start=Path(markdown_output_path).parent)
                img["src"] = relative_path.replace(os.sep, "/")
            else:
                img["src"] = f"../images/{filename}"
    return soup


def replace_code_snippets(
    soup: BeautifulSoup,
    cfg: ConversionConfig,
) -> Tuple[BeautifulSoup, Dict[str, str]]:
    """Replace code blocks with placeholder strings; return updated soup + map.

    Two passes:
      1. Named divs from ``cfg.code_div_lang_map`` (e.g. Revit viewer divs).
      2. Generic ``<pre>`` tags with class-based language detection.
    """
    code_blocks: Dict[str, str] = {}
    counter = 0

    # Pass 1 — profile-specific named divs
    for div_id, lang in cfg.code_div_lang_map.items():
        for div in soup.find_all("div", id=div_id):
            counter += 1
            pre = div.find("pre")
            code_text = pre.get_text() if pre else div.get_text()
            placeholder = f"<<CODE_BLOCK_{counter}>>"
            code_blocks[placeholder] = f"```{lang}\n{code_text}\n```\n"
            div.replace_with(soup.new_string(placeholder))

    # Pass 2 — generic <pre> tags
    _CLASS_LANG = {
        "csharp": "csharp", "cs": "csharp",
        "vb": "vb",
        "cpp": "cpp", "c++": "cpp",
        "fsharp": "fsharp", "fs": "fsharp",
        "xml": "xml", "html": "xml",
        "json": "json",
        "python": "python", "py": "python",
        "java": "java",
        "javascript": "javascript", "js": "javascript",
        "typescript": "typescript", "ts": "typescript",
        "bash": "bash", "shell": "bash", "sh": "bash",
        "sql": "sql",
    }
    for pre in soup.find_all("pre"):
        counter += 1
        code_text = pre.get_text()
        lang = "text"
        class_str = " ".join(pre.get("class", [])).lower()
        for key, mapped in _CLASS_LANG.items():
            if key in class_str:
                lang = mapped
                break
        placeholder = f"<<CODE_BLOCK_{counter}>>"
        code_blocks[placeholder] = f"```{lang}\n{code_text}\n```\n"
        pre.replace_with(soup.new_string(placeholder))

    return soup, code_blocks
