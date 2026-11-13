from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TextIO


@dataclass(frozen=True)
class TextStats:
    lines: int
    words: int
    chars: int
    compact: int


def describe_error(error: OSError) -> str:
    return error.strerror or str(error)


class NotesFile:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._handle: TextIO | None = None

    def switch_to(self, path: Path) -> None:
        handle = path.open("a+", encoding="utf-8", errors="replace")
        self.close()
        self._handle = handle
        self.path = path

    def close(self) -> None:
        if self._handle is not None:
            self._handle.close()
            self._handle = None

    def read(self) -> str:
        handle = self._require_open()
        handle.flush()
        handle.seek(0)
        return handle.read()

    def append(self, line: str) -> None:
        handle = self._require_open()
        handle.write(line + "\n")
        handle.flush()

    def rewrite(self, text: str) -> None:
        handle = self._require_open()
        handle.flush()
        handle.seek(0)
        handle.truncate()
        if text:
            handle.write(text)
        handle.flush()

    def delete_last_line(self) -> bool:
        lines = self.read().splitlines(keepends=True)
        if not lines:
            return False
        lines.pop()
        self.rewrite("".join(lines))
        return True

    def clear(self) -> None:
        self.rewrite("")

    def stats(self) -> TextStats | None:
        text = self.read()
        if not text.strip():
            return None
        return TextStats(
            lines=len(text.splitlines()),
            words=len(text.split()),
            chars=len(text),
            compact=len("".join(text.split())),
        )

    def _require_open(self) -> TextIO:
        if self._handle is None:
            raise RuntimeError("notes file is not opened")
        return self._handle
