from pathlib import Path
import sys

from colorama import Fore, just_fix_windows_console


def get_dir_structure(
    path: str, indent: str = "", without_service_files: bool = False
) -> str:

    try:
        if (
            not path
            or not isinstance(path, str)
            or not Path(path).exists()
            or not Path(path).is_dir()
        ):
            print("No proper directory path provided")
            return ""

        dir_structure = ""
        for item in Path(path).iterdir():
            if without_service_files and item.name.startswith((".", "_")):
                continue

            if item.is_dir():
                dir_structure += f"\n{indent}{Fore.BLUE}{item.name}{Fore.RESET}"
                dir_structure += get_dir_structure(
                    f"{path}/{item.name}",
                    indent=indent + "\t",
                    without_service_files=without_service_files,
                )
                continue

            dir_structure += f"\n{indent}{Fore.GREEN}{item.name}{Fore.RESET}"
        return dir_structure
    except FileNotFoundError:
        print(f"Could not read file or directory '{path}'")
        return ""
    except OSError as error:
        print(f"Could not read directory '{path}': {error}")
        return ""


if __name__ == "__main__":
    just_fix_windows_console()
    path = sys.argv[1] if len(sys.argv) > 1 else input("Enter directory path: ")
    without_service_files = (
        "--without_service_files" in sys.argv[2:] or sys.argv[2] == "True"
        if len(sys.argv) > 2
        else False
    )

    print(get_dir_structure(path, without_service_files=without_service_files))
