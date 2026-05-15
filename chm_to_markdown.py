"""CHM to Markdown converter — CLI entry point.

Usage examples
--------------
  python chm_to_markdown.py                        # interactive menu
  python chm_to_markdown.py --single docs.chm      # single file
  python chm_to_markdown.py --all                  # all CHM in resources/
  python chm_to_markdown.py --all --profile revit  # Revit API docs preset
  python chm_to_markdown.py --all --workers 4 --batch-size 25
"""

import argparse
import asyncio
import os
import shutil

from chm_converter import PROFILES, process_all_chm_files, process_chm_file
from chm_converter.config import DEFAULT_CONFIG

_BANNER = (
    "CHM to Markdown Converter\n"
    "Author : Duong Tran Quang (DTDucas) — baymax.contact@gmail.com\n"
    "GitHub : https://github.com/DTDucas/chm-converter\n"
    "License: MIT\n"
)

RESOURCES_FOLDER = "resources"
BASE_INPUT_FOLDER = "extracted"
BASE_OUTPUT_FOLDER = "output"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Convert CHM files to Markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--single", "-s", metavar="FILE",
                   help="Process a single CHM file")
    p.add_argument("--all", "-a", action="store_true",
                   help="Process all CHM files in the resources folder")
    p.add_argument("--profile", "-p", choices=list(PROFILES.keys()),
                   default="generic",
                   help="Conversion profile: 'generic' (default) or 'revit'")
    p.add_argument("--keep-html", "-k", action="store_true",
                   help="Keep extracted HTML files after conversion")
    p.add_argument("--workers", "-w", type=int, default=8,
                   help="Worker threads for CPU-bound conversion (default: 8)")
    p.add_argument("--batch-size", "-b", type=int, default=50,
                   help="Files per async batch (default: 50)")
    p.add_argument("--semaphore", type=int, default=20,
                   help="Max concurrent I/O operations (default: 20)")
    p.add_argument("--preserve-structure", action="store_true",
                   help=(
                       "Mirror the CHM's internal folder hierarchy in the output data/ "
                       "directory and preserve relative links between files. "
                       "Default is to flatten all pages into a single data/ directory."
                   ))
    return p


async def _run_single(chm_path: str, args: argparse.Namespace, cfg) -> None:
    if not os.path.exists(chm_path):
        candidate = os.path.join(RESOURCES_FOLDER, chm_path)
        if os.path.exists(candidate):
            chm_path = candidate
        else:
            print(f"CHM file not found: {chm_path}")
            return
    await process_chm_file(
        chm_path,
        BASE_INPUT_FOLDER,
        BASE_OUTPUT_FOLDER,
        cfg=cfg,
        max_workers=args.workers,
        semaphore_limit=args.semaphore,
        batch_size=args.batch_size,
        keep_html=args.keep_html,
        preserve_structure=args.preserve_structure,
    )


async def _run_all(args: argparse.Namespace, cfg) -> None:
    await process_all_chm_files(
        RESOURCES_FOLDER,
        BASE_INPUT_FOLDER,
        BASE_OUTPUT_FOLDER,
        cfg=cfg,
        max_workers=args.workers,
        semaphore_limit=args.semaphore,
        batch_size=args.batch_size,
        keep_html=args.keep_html,
        preserve_structure=args.preserve_structure,
    )


async def _interactive(args: argparse.Namespace, cfg) -> None:
    chm_files = [f for f in os.listdir(RESOURCES_FOLDER) if f.lower().endswith(".chm")]
    if not chm_files:
        print(f"No CHM files found in '{RESOURCES_FOLDER}/'. Add CHM files and retry.")
        return

    print("Available CHM files:")
    for i, name in enumerate(chm_files, 1):
        print(f"  {i}. {name}")

    choice = input("\nEnter number to convert, or 'a' for all: ").strip()
    if choice.lower() in ("a", "all"):
        await _run_all(args, cfg)
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(chm_files):
                await _run_single(os.path.join(RESOURCES_FOLDER, chm_files[idx]), args, cfg)
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Enter a number or 'a'.")


async def main() -> None:
    print(_BANNER)
    args = _build_parser().parse_args()
    cfg = PROFILES.get(args.profile, DEFAULT_CONFIG)
    print(f"Profile: {args.profile}")

    os.makedirs(BASE_OUTPUT_FOLDER, exist_ok=True)

    if args.single:
        await _run_single(args.single, args, cfg)
    elif args.all:
        await _run_all(args, cfg)
    else:
        await _interactive(args, cfg)

    if not args.keep_html and os.path.exists(BASE_INPUT_FOLDER):
        shutil.rmtree(BASE_INPUT_FOLDER)

    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
