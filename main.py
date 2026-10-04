import colorama
from colorama import Fore, Style
colorama.just_fix_windows_console()

choice = input(f'pick your color {Fore.RED}RED(1){Style.RESET_ALL} {Fore.GREEN}Green(2){Style.RESET_ALL}: ')
color = {'1': Fore.RED, '2': Fore.GREEN}.get(choice, Style.RESET_ALL)

filename = input("Enter file name (default notes.txt): ").strip() or "notes.txt"
print(f'File name: {filename}')
print('Commands: :q - quit, :show - show file')
try:
    with open(filename, "a+", encoding="utf-8") as file:
        while True:
            line = input(color)
            if line == ':q':
                break
            elif line == ':show':
                file.seek(0)
                print(Style.RESET_ALL + file.read())
                file.seek(0, 2)
            else:
                file.write(line + "\n")
                file.flush()
    print(f'{Style.RESET_ALL}Saved!')

except (KeyboardInterrupt, EOFError):
    print(f"{Style.RESET_ALL}\nExiting... Saved!")
finally:
    print(Style.RESET_ALL, end='')
