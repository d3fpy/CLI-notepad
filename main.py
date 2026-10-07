import colorama
from colorama import Fore, Style
colorama.just_fix_windows_console()

choice = input(f'pick your color {Fore.RED}Red(1){Style.RESET_ALL} {Fore.GREEN}Green(2){Style.RESET_ALL} '
               f'{Fore.CYAN}Blue(3):{Style.RESET_ALL} ')
color = {'1': Fore.RED, '2': Fore.GREEN, '3': Fore.CYAN}.get(choice, Style.RESET_ALL)

filename = input("Enter file name (default notes.txt): ").strip() or "notes.txt"
print(f'File name: {filename}')
print('Commands: :q - quit, :show - show file, :d - deleting the last line')
print(':stats - shows stats about text in file, :clear - wipe all text in file')
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

            elif line == ':d':
                file.seek(0)
                lines = file.readlines()
                if lines:
                    lines.pop()
                    file.seek(0)
                    file.truncate(0)
                    file.writelines(lines)
                    print(f"{Style.RESET_ALL}[last line deleted]")
                else:
                    print(f"{Style.RESET_ALL}[file is already empty]")
            elif line == ":stats":
                file.seek(0)
                text = file.read()
                lines_count = text.count('\n')
                words_count = len(text.split())
                print(f'{Style.RESET_ALL}lines:{lines_count } words:{words_count}, chars: {len(text)}')
            elif line == ':clear':
                confirm = input(f"{Style.RESET_ALL} you really wanna wipe file?(y/n): ")
                if confirm.lower() == 'y':
                    file.seek(0)
                    file.truncate(0)
                    print("[file wiped clean]")

            else:
                file.seek(0,2)
                file.write(line + "\n")
                file.flush()
    print(f'{Style.RESET_ALL}Saved!')

except (KeyboardInterrupt, EOFError):
    print(f"{Style.RESET_ALL}\nExiting... Saved!")
finally:
    print(Style.RESET_ALL, end='')
