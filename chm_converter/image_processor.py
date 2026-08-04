"""Resolve, download, and materialize images referenced by CHM documentation.

Images can come from three sources:
  - Local files extracted from the CHM (relative/absolute paths).
  - Remote URLs (``http://`` / ``https://``).
  - Inline ``data:`` URIs.

Regardless of source, the resulting binary content is hashed with MD5 and
stored once in a single flat ``images`` directory using ``<md5>.<ext>`` as
the filename. Identical content is therefore only ever stored once.
"""

import base64
import hashlib
import mimetypes
import os
import threading
from typing import Optional
from urllib.parse import urlparse

import requests

# Map of MIME type -> file extension (including the leading dot).
MIME_TO_EXT = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
    "image/webp": ".webp",
    "image/bmp": ".bmp",
    "image/x-icon": ".ico",
    "image/vnd.microsoft.icon": ".ico",
}

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}


def _ext_from_mime(mime: Optional[str]) -> Optional[str]:
    if not mime:
        return None
    mime = mime.split(";")[0].strip().lower()
    if mime in MIME_TO_EXT:
        return MIME_TO_EXT[mime]
    guessed = mimetypes.guess_extension(mime)
    if guessed:
        if guessed == ".jpe":
            return ".jpg"
        return guessed
    return None


def _ext_from_url(url: str) -> Optional[str]:
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext in SUPPORTED_EXTENSIONS:
        return ext
    return None


class ImageStore:
    """Materializes images into a single flat directory, deduplicated by MD5."""

    def __init__(self, images_folder: str, timeout: int = 15):
        self.images_folder = images_folder
        self.timeout = timeout
        self._lock = threading.Lock()
        self._known_hashes = set()
        os.makedirs(images_folder, exist_ok=True)

    # -- storage -----------------------------------------------------------
    def _save(self, content: bytes, ext: str) -> str:
        digest = hashlib.md5(content).hexdigest()
        filename = f"{digest}{ext}"
        if digest not in self._known_hashes:
            with self._lock:
                if digest not in self._known_hashes:
                    dest = os.path.join(self.images_folder, filename)
                    if not os.path.exists(dest):
                        with open(dest, "wb") as f:
                            f.write(content)
                    self._known_hashes.add(digest)
        return filename

    # -- sources -------------------------------------------------------------
    def process_local(self, src: str, html_file_path: str) -> Optional[str]:
        """Resolve *src* relative to *html_file_path* and store the file."""
        try:
            base_dir = os.path.dirname(html_file_path)
            clean_src = src.split("#")[0].split("?")[0]
            local_path = os.path.normpath(os.path.join(base_dir, clean_src))
            if not os.path.isfile(local_path):
                print(f"Image not found locally: {local_path}")
                return None
            ext = os.path.splitext(local_path)[1].lower()
            if ext not in SUPPORTED_EXTENSIONS:
                ext = ext or ".png"
            with open(local_path, "rb") as f:
                content = f.read()
            return self._save(content, ext)
        except Exception as exc:
            print(f"Error reading local image '{src}': {exc}")
            return None

    def process_remote(self, url: str) -> Optional[str]:
        """Download *url* and store the resulting binary content."""
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            content = response.content
            ext = _ext_from_url(url)
            if not ext:
                content_type = response.headers.get("Content-Type", "")
                ext = _ext_from_mime(content_type)
            if not ext:
                ext = ".png"
            return self._save(content, ext)
        except Exception as exc:
            print(f"Error downloading remote image '{url}': {exc}")
            return None

    def process_data_uri(self, uri: str) -> Optional[str]:
        """Decode a ``data:`` URI and store the resulting binary content."""
        try:
            if not uri.startswith("data:"):
                return None
            header, _, data = uri.partition(",")
            if not data:
                return None
            meta = header[len("data:"):]
            mime = meta.split(";")[0] or "image/png"
            is_base64 = "base64" in meta
            if is_base64:
                content = base64.b64decode(data, validate=False)
            else:
                from urllib.parse import unquote_to_bytes
                content = unquote_to_bytes(data)
            ext = _ext_from_mime(mime) or ".png"
            return self._save(content, ext)
        except Exception as exc:
            print(f"Error decoding inline data image: {exc}")
            return None

    # -- dispatch --------------------------------------------------------
    def process(self, src: str, html_file_path: Optional[str]) -> Optional[str]:
        """Materialize *src* and return the stored filename, or *None* on failure."""
        if not src:
            return None
        if src.startswith("data:"):
            return self.process_data_uri(src)
        parsed = urlparse(src)
        if parsed.scheme in ("http", "https"):
            return self.process_remote(src)
        if html_file_path:
            return self.process_local(src, html_file_path)
        return None
