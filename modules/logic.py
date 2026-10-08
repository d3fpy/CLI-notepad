import os
from colorama import Fore, Style

def main():

    filename = (
        input("Enter file name (default notes.txt): ").strip() or "notes.txt"
    )

    if not os.path.exists(filename):
        open(filename, "a").close()

    choice = input(
        f"pick your color {Fore.RED}Red(1){Style.RESET_ALL} {Fore.GREEN}Green(2){Style.RESET_ALL} "
        f"{Fore.CYAN}Blue(3):{Style.RESET_ALL} {Fore.MAGENTA} Purple(4) {Style.RESET_ALL} "
    )
    
    color = {"1": Fore.RED, "2": Fore.GREEN, "3": Fore.CYAN, '4': Fore.MAGENTA}.get(
        choice, Style.RESET_ALL
    )
    
    file_inner = f"[{filename}]".center(19)
    colored_file = file_inner.replace(f"[{filename}]", f"{Fore.YELLOW}[{filename}]{Style.RESET_ALL}")

    print("         ┌───────────────────┐")
    print("         │    -- FILE --     │")
    print(f"         │{colored_file}│")
    print("         └─────────┬─────────┘")
    print("                   |")
    print("┌───────────────────────────────────────┐")
    print("█             -- SYSTEM --              █")
    print("█  :q      - quit                       █")
    print("█  :show   - show file contents         █")
    print("└──────────────────┬────────────────────┘")
    print("                   |")
    print("┌──────────────────┴────────────────────┐")
    print("█              -- TEXT --               █")
    print("█  :d      - delete the last line       █")
    print("█  :stats  - show stats about text      █")
    print("█  :clear  - wipe all text in file      █")
    print("█  :find   - find any text in file      █")
    print("└───────────────────────────────────────┘")
    try:
        with open(filename, "a+", encoding="utf-8") as file:
            while True:
                line = input(color)

                match line:
                    case ":q":
                        break

                    case ":show":
                        file.flush()
                        file.seek(0)
                        content = file.read()
                        print(Style.RESET_ALL + file.read())
                        file.seek(0, 2)

                        if not content:
                            print('[file is empty]')

                        else:
                            print(Style.RESET_ALL + content, end="")

                        file.seek(0, 2)

                    case ":d":
                        file.seek(0)
                        lines = file.readlines()

                        if lines:
                            lines.pop()
                            file.seek(0)
                            file.truncate(0)
                            file.writelines(lines)
                            file.flush()
                            print(f"{Style.RESET_ALL}[last line deleted]")
                        else:
                            print(
                                f"{Style.RESET_ALL}[file is already empty]"
                            )

                    case ":stats":
                        file.seek(0)
                        text = file.read()
                        lines_count = (
                            len(text.splitlines()) if text.strip() else 0
                        )
                        words_count = len(text.split())
                        print(
                            f"{Style.RESET_ALL}lines: {lines_count} | words: {words_count} | chars: {len(text)}"
                        )
                        file.seek(0, 2)
                        if not text:
                            print(f"{Style.RESET_ALL}[file is empty]")

                    case ":clear":
                        confirm = input(
                            f"{Style.RESET_ALL}you really wanna wipe file?(y/n): "
                        )
                        if confirm.lower() == "y":
                            file.seek(0)
                            file.truncate(0)
                            file.flush()
                            print(f"{Style.RESET_ALL}[file has been wiped]")
                    case ":find":
                        keyword = input(
                            f"{Style.RESET_ALL}enter word to find: "
                        )
                        file.seek(0)
                        found = False
                        for i, l in enumerate(file, 1):
                            if keyword in l:
                                print(
                                    f"Line {i}: {l.strip().replace(keyword, Fore.YELLOW + keyword + Style.RESET_ALL)}"
                                )
                                found = True
                        if not found:
                            print(f"{Style.RESET_ALL}[no matches found]")
                        file.seek(0, 2)
                        
                    case "":
                        continue

                    case _:
                        file.seek(0, 2)
                        file.write(line + "\n")
                        file.flush()
                        
    except (KeyboardInterrupt, EOFError):
        print(f"{Style.RESET_ALL}\nExiting... Saved!")
    finally:
        print(Style.RESET_ALL, end="")

    return filename

if __name__ == "__main__":
    main()
