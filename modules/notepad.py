from __future__ import annotations

import re
from pathlib import Path

from colorama import Fore

from . import ui
from .constants import ALIASES, DEFAULT_COLOR
from .storage import NotesFile, describe_error


class Notepad:

    def __init__(self, path: Path, color: str = DEFAULT_COLOR) -> None:
        self.color = color
        self.notes = NotesFile(path)
        self._handlers = {
            ":show": self.show,
            ":stats": self.show_stats,
            ":find": self.find,
            ":d": self.delete_last_line,
            ":clear": self.clear,
            ":help": ui.print_commands,
        }

    @property
    def path(self) -> Path:
        return self.notes.path

    def run(self) -> None:
        try:
            self.notes.switch_to(self.path)
        except OSError as error:
            ui.message(f"[cannot open {self.path}: {describe_error(error)}]")
            return

        ui.print_header(self.path)
        try:
            while self._handle(input(self.color)):
                pass
        except (KeyboardInterrupt, EOFError):
            print()
        finally:
            self.notes.close()
            ui.message("Exiting... Saved!")

    def _handle(self, line: str) -> bool:
        if not line:
            return True

        if not line.startswith(":"):
            self.notes.append(line)
            return True

        command, _, argument = line.partition(" ")
        command = command.strip().lower()
        command = ALIASES.get(command, command)

        if command == ":q":
            return False
        if command == ":open":
            self._open_file(argument)
            return True

        handler = self._handlers.get(command)
        if handler is None:
            ui.message(f"[unknown command: {command}] type :help for the list")
        else:
            handler()
        return True

    def _open_file(self, argument: str) -> None:
        name = argument.strip() or ui.ask("switch to file: ").strip()
        if not name:
            ui.message("[cancelled]")
            return
        try:
            self.notes.switch_to(Path(name.strip('"')))
        except OSError as error:
            ui.message(f"[cannot open {name}: {describe_error(error)}]")
            return
        ui.print_header(self.path)

    def show(self) -> None:
        content = self.notes.read()
        if not content:
            ui.message("[file is empty]")
            return
        ui.print_content(content)

    def show_stats(self) -> None:
        stats = self.notes.stats()
        if stats is None:
            ui.message("[file is empty]")
            return
        ui.message(
            f"lines: {stats.lines} | words: {stats.words} | chars: {stats.chars} | "
            f"chars without spaces: {stats.compact}"
        )

    def delete_last_line(self) -> None:
        if self.notes.delete_last_line():
            ui.message("[last line deleted]")
        else:
            ui.message("[file is already empty]")

    def clear(self) -> None:
        if not ui.confirm("you really wanna wipe file?(y/n): "):
            ui.message("[cancelled]")
            return
        self.notes.clear()
        ui.message("[file has been wiped]")

    def find(self) -> None:
        keyword = ui.ask("enter word to find: ").strip()
        if not keyword:
            ui.message("[search cancelled: empty word]")
            return

        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        matches = [
            (number, line)
            for number, line in enumerate(self.notes.read().splitlines(), 1)
            if pattern.search(line)
        ]
        if not matches:
            ui.message("[no matches found]")
            return

        for number, line in matches:
            highlighted = pattern.sub(
                lambda match: f"{Fore.YELLOW}{match.group(0)}{self.color}", line
            )
            ui.message(f"line {number}: {highlighted}")
        ui.message(f"[{len(matches)} match(es) found]")
