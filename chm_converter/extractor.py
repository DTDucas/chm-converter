import asyncio
import os
import platform
import shutil


def clear_folder(folder_path: str) -> None:
    """Delete all contents of *folder_path*, creating it if absent."""
    if os.path.exists(folder_path):
        for name in os.listdir(folder_path):
            path = os.path.join(folder_path, name)
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)
                else:
                    shutil.rmtree(path)
            except Exception as exc:
                print(f"Warning: could not delete {path}: {exc}")
    else:
        os.makedirs(folder_path)


def _find_7zip() -> str | None:
    """Return the path to a usable 7-Zip executable, or *None* if not found.

    Search order on Windows:
      1. Default install path  C:\\Program Files\\7-Zip\\7z.exe
      2. PATH entries: 7z, 7za, 7zz

    Search order on Linux / macOS:
      PATH entries: 7z, 7zz, 7za
    """
    if platform.system() == "Windows":
        default = r"C:\Program Files\7-Zip\7z.exe"
        if os.path.exists(default):
            return default
        for name in ("7z", "7za", "7zz"):
            found = shutil.which(name)
            if found:
                return found
        return None

    for name in ("7z", "7zz", "7za"):
        found = shutil.which(name)
        if found:
            return found
    return None


async def export_chm_to_htm(chm_path: str, export_folder: str) -> bool:
    """Extract *chm_path* into *export_folder* using 7-Zip.

    Returns *True* on success, *False* on failure.
    """
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    clear_folder(export_folder)

    seven_zip = _find_7zip()
    if not seven_zip:
        if platform.system() == "Windows":
            print("7z.exe not found. Install 7-Zip from https://www.7-zip.org/")
        else:
            print("7z not found. Install p7zip: sudo apt install p7zip-full")
        return False

    try:
        process = await asyncio.create_subprocess_exec(
            seven_zip, "x", chm_path, f"-o{export_folder}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        _, stderr = await process.communicate()
        if process.returncode != 0:
            print(f"7-Zip error extracting {chm_path}:\n{stderr.decode(errors='replace')}")
            return False
        return True
    except Exception as exc:
        print(f"Failed to run 7-Zip on {chm_path}: {exc}")
        return False


def find_html_folder(base_folder: str) -> str | None:
    """Return the root folder from which HTML files should be collected.

    Search order:
      1. ``<base_folder>/html/``  — Autodesk / Microsoft CHM layout
      2. ``<base_folder>/``       — flat layout (HTML at root level)
      3. Recursive walk           — complex layouts (e.g. DirectX SDK, issue #10)
                                    returns *base_folder* so callers can ``os.walk``

    Returns *None* only when no HTML files exist anywhere in the tree.
    """
    # 1. Standard html/ subfolder
    candidate = os.path.join(base_folder, "html")
    if os.path.exists(candidate):
        return candidate

    # 2. Flat: HTML files directly at base level
    try:
        if any(f.lower().endswith((".htm", ".html")) for f in os.listdir(base_folder)):
            return base_folder
    except OSError:
        return None

    # 3. Recursive fallback: HTML files exist somewhere deeper in the tree
    for _, _, files in os.walk(base_folder):
        if any(f.lower().endswith((".htm", ".html")) for f in files):
            return base_folder  # callers use os.walk from here

    return None
