# CHM to Markdown Converter

A Python utility for converting Compiled HTML Help (`.chm`) files into clean Markdown, with built-in support for multiple document types through a profile system.

Originally built for Autodesk Revit API documentation; the generic profile works with any CHM file.

## Features

- **Profile-based conversion** — `generic` profile for any CHM, `revit` profile for Autodesk Revit API docs
- **Auto encoding detection** — handles UTF-8, GB18030, GBK, GB2312, and more via `chardet`
- **Cross-platform 7-Zip detection** — finds `7z`/`7za`/`7zz` on PATH (Windows, Linux, macOS)
- **Flexible CHM structure support** — handles `html/` subdirectory, flat, and deeply nested layouts (e.g. DirectX SDK)
- **`--preserve-structure`** — optionally mirrors the CHM's internal folder hierarchy in the output instead of flattening everything into `data/`
- **Code block preservation** — detects language from class names and named divs; supports C#, VB, C++, F#, Python, Java, JS/TS, Bash, SQL, XML, JSON
- **Table normalization** — cleans and re-formats Markdown tables
- **Index generation** — produces `file_index.json`, `id_lookup.json`, and `index.md` for search and AI integration
- **Async + batched processing** — bounded concurrency and periodic GC prevent memory overflow on large CHM files (6 000+ pages)

## Project Structure

```
chm_converter/           # Core package
├── config.py            # ConversionConfig dataclass + built-in profiles
├── encoding.py          # Encoding detection (chardet + CJK fallbacks)
├── extractor.py         # CHM extraction via 7-Zip; HTML folder detection
├── html_processor.py    # HTML cleaning, link rewriting, code block extraction
├── md_converter.py      # HTML → Markdown conversion + post-processing
├── indexer.py           # File dictionary building + index file generation
└── pipeline.py          # High-level async pipeline (process_chm_file, process_all_chm_files)

chm_to_markdown.py       # CLI entry point
resources/               # Place CHM files here
output/                  # Generated Markdown (created automatically)
```

### Output layout

```
output/
└── <name>/
    ├── core/
    │   ├── file_index.json   # id → {title, filename, version}
    │   ├── id_lookup.json    # lowercase id → {title, filename, keywords, version}
    │   └── index.md          # alphabetical navigation page
    └── data/
        ├── Topic1.md
        ├── Topic2.md
        └── ...
```

## Requirements

- Python 3.10+
- [7-Zip](https://www.7-zip.org/) — `7z` must be reachable via the default install path or `PATH`
  - Windows: installs to `C:\Program Files\7-Zip\7z.exe` by default, or add to `PATH`
  - Linux: `sudo apt install p7zip-full`
  - macOS: `brew install p7zip`

## Installation

```bash
git clone https://github.com/DTDucas/chm-converter.git
cd chm-converter
pip install -r requirements.txt
```

## Usage

Place `.chm` files in the `resources/` folder, then run:

```bash
# Interactive menu (lists available CHM files)
python chm_to_markdown.py

# Convert a single file
python chm_to_markdown.py --single resources/docs.chm

# Convert all CHM files in resources/
python chm_to_markdown.py --all

# Use the Revit API profile (strips Revit help-viewer boilerplate)
python chm_to_markdown.py --all --profile revit

# Preserve the original folder hierarchy inside data/ (e.g. for DirectX SDK)
python chm_to_markdown.py --single resources/directx_sdk.chm --preserve-structure

# Keep extracted HTML for debugging
python chm_to_markdown.py --single resources/docs.chm --keep-html

# Tune performance
python chm_to_markdown.py --all --workers 4 --batch-size 25 --semaphore 10
```

### CLI arguments

| Argument               | Short | Default   | Description                                                     |
| ---------------------- | ----- | --------- | --------------------------------------------------------------- |
| `--single FILE`        | `-s`  | —         | Convert a single CHM file                                       |
| `--all`                | `-a`  | —         | Convert all CHM files in `resources/`                           |
| `--profile`            | `-p`  | `generic` | Conversion profile: `generic` or `revit`                        |
| `--keep-html`          | `-k`  | off       | Retain extracted HTML after conversion                          |
| `--workers N`          | `-w`  | `8`       | Thread-pool size for CPU-bound conversion                       |
| `--batch-size N`       | `-b`  | `50`      | Files processed per async batch                                 |
| `--semaphore N`        | —     | `20`      | Max concurrent I/O operations                                   |
| `--preserve-structure` | —     | off       | Mirror CHM folder hierarchy in `data/`; preserve relative links |

## Profiles

| Profile   | Description                                                                                                            |
| --------- | ---------------------------------------------------------------------------------------------------------------------- |
| `generic` | Minimal cleanup — works with any CHM file                                                                              |
| `revit`   | Strips Autodesk Revit help-viewer UI chrome (collapsible regions, feedback links, code-tab toolbars, boilerplate text) |

Custom profiles can be created programmatically:

```python
from chm_converter.config import ConversionConfig
from chm_converter.pipeline import process_chm_file
import asyncio

cfg = ConversionConfig(
    classes_to_remove=["my-nav-bar", "site-footer"],
    ids_to_remove=["cookie-banner"],
    cleanup_patterns=[
        (r"Rate this article.*?---", "---"),
    ],
)

asyncio.run(process_chm_file("docs.chm", "extracted", "output", cfg=cfg))
```

## AI Integration

The `core/` folder is designed for RAG and AI search pipelines:

- `file_index.json` — maps every file ID to its title, filename, and version
- `id_lookup.json` — lowercase-keyed with extracted keyword lists for full-text search
- `index.md` — human-readable alphabetical index with anchor links

## Troubleshooting

| Problem                                         | Solution                                                                                   |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `7z not found`                                  | Install 7-Zip and ensure it is on `PATH`; see Requirements above                           |
| Empty output / `No HTML files found`            | CHM uses a nested folder layout — add `--preserve-structure` to enable recursive traversal |
| Revit 2025+ pages contain only a title, no body | Fixed in current version: `TopicContent` is no longer stripped from the Revit profile      |
| Garbled CJK text                                | The tool auto-detects encoding via `chardet`; try `--profile generic` if issues persist    |
| Memory errors on large CHM                      | Reduce `--workers` and `--batch-size`                                                      |
| Permission errors                               | Run the terminal with administrator / sudo privileges                                      |

## License

MIT License

## Author

**Duong Tran Quang (DTDucas)**
baymax.contact@gmail.com
[github.com/DTDucas](https://github.com/DTDucas)
Author: [dtducas.com](https://dtducas.com)

### Contributors

- **Jiangxumin** — Chinese encoding support, cross-platform 7-Zip detection, memory-safe batch processing ([PR #11](https://github.com/DTDucas/chm-converter/pull/11))
