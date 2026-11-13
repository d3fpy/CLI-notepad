from colorama import Fore, Style

DEFAULT_FILENAME = "notes.txt"
DEFAULT_COLOR = Style.RESET_ALL
SEPARATOR = "-" * 33

COLOR_CHOICES: dict[str, tuple[str, str]] = {
    "1": ("Red", Fore.RED),
    "2": ("Green", Fore.GREEN),
    "3": ("Blue", Fore.CYAN),
    "4": ("Purple", Fore.MAGENTA),
}

COMMANDS: dict[str, str] = {
    ":show": "show file contents",
    ":stats": "show stats about text",
    ":find": "find text in file (case-insensitive)",
    ":d": "delete the last line",
    ":clear": "wipe all text in file",
    ":open <file>": "switch to another file",
    ":help": "show this list",
    ":q": "save and quit",
}

ALIASES: dict[str, str] = {
    ":h": ":help",
    ":quit": ":q",
    ":delete": ":d",
}
