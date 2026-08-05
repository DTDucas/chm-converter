from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class ConversionConfig:
    """All parameters controlling how HTML content is cleaned and converted.

    Create a custom instance or use one of the built-in profiles:
      - DEFAULT_CONFIG  — sensible generic defaults
      - REVIT_CONFIG    — tuned for Autodesk Revit API help files
    """

    # HTML tags to strip entirely (content discarded)
    tags_to_remove: List[str] = field(default_factory=lambda: [
        "iframe", "object", "script", "br", "meta", "link", "input",
    ])

    # CSS classes whose elements are stripped
    classes_to_remove: List[str] = field(default_factory=list)

    # Element IDs whose elements are stripped
    ids_to_remove: List[str] = field(default_factory=list)

    # Maps div/@id values to fenced-code language names.
    # Used for CHM viewers that wrap code samples in named divs.
    code_div_lang_map: Dict[str, str] = field(default_factory=dict)

    # Extra (pattern, replacement) pairs applied to the final Markdown text
    # after the standard generic cleanup.  Use re.DOTALL patterns with care.
    cleanup_patterns: List[Tuple[str, str]] = field(default_factory=list)

    # html2text rendering options
    body_width: int = 0
    ignore_links: bool = False
    ignore_images: bool = False
    ignore_tables: bool = False
    single_line_break: bool = True
    unicode_snob: bool = True


# ---------------------------------------------------------------------------
# Built-in profiles
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = ConversionConfig()

REVIT_CONFIG = ConversionConfig(
    classes_to_remove=[
        "collapsibleAreaRegion",
        "collapsibleRegionTitle",
        "collapseToggle",
        "codeSnippetContainerTab",
        "codeSnippetToolBar",
        "codeSnippetContainerTabs",
        "pageHeader",
        "feedbackLink",
        "userDataStyle",
    ],
    ids_to_remove=[
        "PageFooter",
        "PageHeader",
        # NOTE: "TopicContent" intentionally excluded — in Revit 2025+ it wraps
        # the actual page body, so stripping it removes all content (issue #9).
        "userDataCache",
        "HT_MailLink",
    ],
    # Revit help viewer wraps code samples in divs with these IDs
    code_div_lang_map={
        "IDAB_code_Div1": "csharp",
        "IDAB_code_Div2": "vb",
        "IDAB_code_Div3": "cpp",
        "IDAB_code_Div4": "fsharp",
    },
    # Revit help-viewer boilerplate that leaks into the converted text
    cleanup_patterns=[
        (r"See Also \[Send Feedback\].*?---", "---"),
        (r"Collapse AllExpand All", ""),
        (r"Code: All Code: Multiple.*?---", "---"),
        (r"\[Send comments.*?\].*?\)", ""),
    ],
)

PROFILES: Dict[str, ConversionConfig] = {
    "generic": DEFAULT_CONFIG,
    "revit": REVIT_CONFIG,
}
