from pathlib import Path

from utils.handle_file import handle_file


def get_cats_info(path: str) -> list[dict[str, str]]:
    if (
        not path
        or not isinstance(path, str)
        or not Path(path).exists()
        or not Path(path).is_file()
    ):
        print("No proper file path provided")
        return []

    try:
        with open(path, encoding="utf-8") as file:
            data_rows = [line.strip() for line in file.readlines() if line.strip()]
            cats_info = []
            for row in data_rows:
                splitted_row = row.split(",")
                if len(splitted_row) != 3:
                    print(f"Invalid row format: {row} in file {path}")
                    continue
                cats_info.append(
                    {
                        "id": splitted_row[0],
                        "name": splitted_row[1],
                        "age": splitted_row[2],
                    }
                )
            return cats_info

    except FileNotFoundError:
        print("File not found")
        return []
    except (ValueError, UnicodeDecodeError):
        print("Invalid file data")
        return []
    except OSError as error:
        print(f"Could not read the file: {error}")
        return []


def get_cats_info_2(path: str) -> list[dict[str, str]]:
    def file_handler(file):
        data_rows = [line.strip() for line in file.readlines() if line.strip()]
        return [
            {
                "id": row.split(",")[0],
                "name": row.split(",")[1],
                "age": row.split(",")[2],
            }
            for row in data_rows
            if len(row.split(",")) == 3
        ]

    return handle_file(
        path,
        file_handler,
        error_value=[],
    )
