# CLI-notepad
A tiny console notepad in Python. Type lines, and they are appended to a text file.

## Features

- Choose the input text color (red / green / blue /default)
- Choose the file name (default: `notes.txt`)
- Every line is saved immediately
- View the file contents without leaving the program

## Install

```
pip install -r requirements.txt
```

## Run

```
python main.py
```

## Commands

| Command | Action |
|---------|--------|
| `:show` | Show the file contents |
| `:q`    | Save and quit |
| `:stats`    |  shows stats about text in file |
| `:clear`    |  wipes all text in file |
| `:find`    |  find any text in file |


`Ctrl+C` also exits safely.

## License

[![Licence](https://img.shields.io/badge/License-GNU-brightgreen?style=for-the-badge)](./LICENSE)
