from pathlib import Path
import sys

from get_cats_info import get_cats_info, get_cats_info_2
from get_dir_structure import get_dir_structure
from total_salary import total_salary
from colorama import just_fix_windows_console


def main() -> None:
    # Завдання 1
    print("\nЗавдання 1\n")
    total, average = total_salary("data/salary_file.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}\n"
    )

    # Завдання 2
    print("\nЗавдання 2\n")
    cats_info = get_cats_info("data/cats_file.txt")
    cats_info_2 = get_cats_info_2("data/cats_file.txt")
    print("Cats: ", cats_info)
    print("Cats_2: ", cats_info_2)

    # Завдання 3
    print("\nЗавдання 3\n")
    just_fix_windows_console()
    # for use sys args call get_dir_structure.py with args: path and optional --without_service_files from command line
    print(
        get_dir_structure(
            input("Enter directory path: "),
            without_service_files=(
                "--without_service_files" in sys.argv[2:] or sys.argv[2] == "True"
                if len(sys.argv) > 2
                else False
            ),
        ),
    )


if __name__ == "__main__":
    main()
