import asyncio

import aiofiles
import chardet

# Preferred encodings tried in order when chardet confidence is low.
# GB18030 is a superset of GBK/GB2312, so it goes first.
_FALLBACK_ENCODINGS = ["gb18030", "gbk", "gb2312", "utf-8"]


def detect_file_encoding(file_path: str) -> str:
    """Return the best-guess encoding for *file_path*.

    Reads the first 10 KB with chardet.  If confidence is below 70 %,
    falls back to probing common CJK encodings before settling on UTF-8.
    """
    try:
        with open(file_path, "rb") as f:
            raw = f.read(10_000)
        result = chardet.detect(raw)
        encoding = result.get("encoding") or "utf-8"
        confidence = result.get("confidence", 0)

        if confidence < 0.7:
            for enc in _FALLBACK_ENCODINGS:
                try:
                    with open(file_path, "r", encoding=enc) as f:
                        f.read(1_000)
                    return enc
                except (UnicodeDecodeError, LookupError):
                    continue
        return encoding
    except OSError:
        pass

    for enc in _FALLBACK_ENCODINGS:
        try:
            with open(file_path, "r", encoding=enc) as f:
                f.read(1_000)
            return enc
        except (UnicodeDecodeError, LookupError):
            continue
    return "utf-8"


async def read_file_with_encoding(file_path: str) -> str:
    """Read *file_path* as text, auto-detecting the encoding."""
    loop = asyncio.get_running_loop()
    encoding = await loop.run_in_executor(None, detect_file_encoding, file_path)
    async with aiofiles.open(file_path, "r", encoding=encoding, errors="replace") as f:
        return await f.read()
