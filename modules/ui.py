from __future__ import annotations

from pathlib import Path

from colorama import Fore, Style

from .constants import (
    COLOR_CHOICES,
    COMMANDS,
    DEFAULT_COLOR,
    DEFAULT_FILENAME,
    SEPARATOR,
)


def ask(prompt: str) -> str:
    return input(f"{Style.RESET_ALL}{prompt}")


def confirm(prompt: str) -> bool:
    return ask(prompt).strip().lower() == "y"


def prompt_filename() -> Path:
    raw = input(f"Enter file name (default {DEFAULT_FILENAME}): ").strip()
    return Path(raw.strip('"') or DEFAULT_FILENAME)


def choose_color() -> str:
    options = " ".join(
        f"{color}{name}({key}){Style.RESET_ALL}"
        for key, (name, color) in COLOR_CHOICES.items()
    )
    answer = input(f"pick your color: {options} plain(5): ").strip()
    choice = COLOR_CHOICES.get(answer)
    return choice[1] if choice else DEFAULT_COLOR


def message(text: str) -> None:
    print(f"{Style.RESET_ALL}{text}")


def print_commands() -> None:
    for name, description in COMMANDS.items():
        print(f" {name:<14} {description}")


def print_header(path: Path) -> None:
    print(f"file: {Fore.YELLOW}[{path}]{Style.RESET_ALL}")
    print(SEPARATOR)
    print_commands()
    print(f"{SEPARATOR}\n")


def print_content(content: str) -> None:
    print(Style.RESET_ALL, end="")
    print(content, end="" if content.endswith("\n") else "\n")