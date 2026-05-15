import re
from typing import Dict, Optional

import html2text
from bs4 import BeautifulSoup

from .config import ConversionConfig, DEFAULT_CONFIG
from .html_processor import (
    extract_page_title,
    remove_unwanted_elements,
    replace_code_snippets,
    update_links,
)

# ---------------------------------------------------------------------------
# Table helpers
# ---------------------------------------------------------------------------

def _fix_table_block(table_lines: list) -> list:
    rows = []
    for line in table_lines:
        cells = [c.strip() for c in line.split("|")]
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        rows.append(cells)

    formatted = []
    for i, row in enumerate(rows):
        formatted.append("| " + " | ".join(row) + " |")
        if i == 0:
            formatted.append("| " + " | ".join(["---"] * len(row)) + " |")
    return formatted


def fix_tables(text: str) -> str:
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        if (
            "|" in lines[i]
            and i + 1 < len(lines)
            and re.match(r"^[\s\-\|:]+$", lines[i + 1])
        ):
            table = []
            while i < len(lines) and "|" in lines[i]:
                table.append(lines[i])
                i += 1
            out.extend(_fix_table_block(table))
            out.append("")
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Generic Markdown cleanup (profile-independent)
# ---------------------------------------------------------------------------

_GUID_PATTERN = re.compile(
    r"\(([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\.md\)"
)
_HEADER_RE = {level: re.compile(r"^#{" + str(level) + r"}([^\s])") for level in range(1, 7)}


def _clean_generic(text: str) -> str:
    """Apply cleanup rules that are safe for all CHM documents."""
    # Collapse 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Ensure a space after heading hashes
    lines = text.splitlines()
    for i, line in enumerate(lines):
        for level, pattern in _HEADER_RE.items():
            if pattern.match(line):
                lines[i] = re.sub(
                    pattern,
                    "#" * level + r" \1",
                    line,
                )
                break
    text = "\n".join(lines)

    # Rename bare GUIDs to reference-<guid> for readability
    text = _GUID_PATTERN.sub(r"(reference-\1.md)", text)

    # Drop orphaned javascript: links that html2text may leave behind
    text = re.sub(r"\[.*?\]\(javascript:.*?\)", "", text)

    # Collapse duplicate horizontal rules
    text = re.sub(r"---\s*---", "---", text)

    return text


def clean_markdown_formatting(text: str, cfg: ConversionConfig = DEFAULT_CONFIG) -> str:
    """Apply generic cleanup then any profile-specific patterns from *cfg*."""
    text = _clean_generic(text)
    for pattern, replacement in cfg.cleanup_patterns:
        text = re.sub(pattern, replacement, text)
    return text


# ---------------------------------------------------------------------------
# Main converter
# ---------------------------------------------------------------------------

def convert_html_to_markdown(
    html_content: str,
    file_dictionary: Optional[Dict] = None,
    version: Optional[str] = None,
    cfg: ConversionConfig = DEFAULT_CONFIG,
    preserve_structure: bool = False,
) -> str:
    """Convert an HTML string to Markdown using *cfg* for cleanup rules."""
    soup = BeautifulSoup(html_content, "html.parser")
    title = extract_page_title(soup)

    soup = remove_unwanted_elements(soup, cfg)
    soup = update_links(soup, file_dictionary, preserve_structure)
    soup, code_blocks = replace_code_snippets(soup, cfg)

    h = html2text.HTML2Text()
    h.body_width = cfg.body_width
    h.ignore_links = cfg.ignore_links
    h.ignore_images = cfg.ignore_images
    h.ignore_tables = cfg.ignore_tables
    h.single_line_break = cfg.single_line_break
    h.unicode_snob = cfg.unicode_snob
    markdown = h.handle(str(soup))

    if title:
        heading = f"# {title} ({version})\n\n" if version else f"# {title}\n\n"
        markdown = heading + markdown

    for placeholder, block in code_blocks.items():
        markdown = markdown.replace(placeholder, block)

    markdown = fix_tables(markdown)
    markdown = clean_markdown_formatting(markdown, cfg)
    return markdown
