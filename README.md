# CLI-notepad

A tiny console notepad in Python. Type lines, and they are appended to a text file.

## Features

- Choose the input text color: red (1) / green (2) / blue (3) / purple (4) / plain (5)
- Choose the file name (default: `notes.txt`) and switch to another file with `:open`
- Every line is saved immediately — nothing is lost on exit
- View, search, measure and trim the file without leaving the program
- `:find` is case-insensitive and highlights matches with line numbers
- `:stats` reports lines, words and characters
- `:d` removes the last line, `:clear` wipes the file after confirmation
- Unknown `:commands` are reported instead of being written into the file
- Bad file paths (missing folder, no permissions) print a clear message instead of a traceback
- `Ctrl+C` / `Ctrl+D` exit safely; the file is always closed properly

## Install

```
pip install -r requirements.txt
```

## Run

```
python main.py
```

Then enter a file name (or press `Enter` for `notes.txt`) and pick a color.
After the header and command list, the prompt is drawn in the chosen color (shown as `>` below):

```
> Hello, world!
> second line
> :stats
lines: 2 | words: 4 | chars: 26 | chars without spaces: 22
> :find
enter word to find: world
line 1: Hello, world!
[1 match(es) found]
> :q
Exiting... Saved!
```

## Commands

| Command | Action |
|---------|--------|
| `:show` | Show the file contents |
| `:stats` | Show stats about text in file (lines / words / chars / chars without spaces) |
| `:find` | Find text in file (case-insensitive, matches highlighted, with line numbers) |
| `:d` | Delete the last line |
| `:clear` | Wipe all text in file (asks `y/n` confirmation) |
| `:open <file>` | Switch to another file (asks for the name if omitted) |
| `:help` | Show the command list |
| `:q` | Save and quit |

Aliases: `:h` = `:help`, `:quit` = `:q`, `:delete` = `:d`.

Notes:

- An empty line is ignored, any other line is written to the file as is.
- Command names are case-insensitive (`:SHOW` works), and a typo like `:shwo` never becomes a note.
- Missing files are created automatically on first use.

`Ctrl+C` also exits safely.

## Project structure

```
main.py                 entry point (sets up colorama, calls modules.logic.main)
modules/__init__.py     package marker
modules/constants.py    defaults, color choices, command table, aliases
modules/ui.py           console prompts, messages, header, content output
modules/storage.py      NotesFile: open/append/read/rewrite and TextStats
modules/notepad.py      session loop, command dispatch and command handlers
modules/logic.py        main(): asks for file and color, starts the session
```

## License

[![Licence](https://img.shields.io/badge/License-GNU-brightgreen?style=for-the-badge)](./LICENSE)
