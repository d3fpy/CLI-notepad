# CLI-notepad


A tiny console notepad in Python. Type lines, and they are appended to a text file.

## Features

- Choose the input text color (red / green / default)
- Choose the file name (default: `notes.txt`)
- Every line is saved immediately
- View the file contents without leaving the program

## Install

```
pip install colorama
```

## Run

```
python notepad.py
```

## Commands

| Command | Action |
|---------|--------|
| `:show` | Show the file contents |
| `:q`    | Save and quit |

`Ctrl+C` also exits safely.

## License

[GNU](https://github.com/d3fpy/CLI-notepad/blob/main/LICENSE)
