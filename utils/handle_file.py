from pathlib import Path


def handle_file(path, file_handler, error_value):
    if (
        not path
        or not isinstance(path, str)
        or not Path(path).exists()
        or not Path(path).is_file()
    ):
        print("No proper file path provided")
        return error_value

    try:
        with open(path, encoding="utf-8") as file:
            return file_handler(file)

    except FileNotFoundError:
        print("File not found")
        return error_value
    except (ValueError, UnicodeDecodeError):
        print("Invalid file data")
        return error_value
    except OSError as error:
        print(f"Could not read the file: {error}")
        return error_value
