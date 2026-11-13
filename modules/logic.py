from . import ui
from .notepad import Notepad


def main() -> None:
    path = ui.prompt_filename()
    color = ui.choose_color()
    Notepad(path, color).run()


if __name__ == "__main__":
    main()
