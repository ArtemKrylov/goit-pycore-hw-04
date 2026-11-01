from pathlib import Path

from utils.handle_file import handle_file


def total_salary(path: str) -> tuple[float, float]:
    error_value = (0.0, 0.0)
    if (
        not path
        or not isinstance(path, str)
        or not Path(path).exists()
        or not Path(path).is_file()
    ):
        print("No proper file path provided")
        return error_value

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            row_data = [line.strip() for line in file.readlines() if line.strip()]
            salaries = [float(row.split(",")[-1]) for row in row_data]
            total_sum = sum(salaries)
            average_salary = (
                total_sum / len(salaries) if salaries and len(salaries) else 0.0
            )
            return (total_sum, average_salary)
    except FileNotFoundError:
        print("File not found")
        return error_value
    except (ValueError, UnicodeDecodeError):
        print("Invalid file data")
        return error_value
    except OSError as error:
        print(f"Could not read the file: {error}")
        return error_value


def total_salary_2(path: str) -> tuple[float, float]:
    def file_handler(file):
        row_data = [line.strip() for line in file.readlines() if line.strip()]
        salaries = [float(row.split(",")[-1]) for row in row_data]
        total_sum = sum(salaries)
        average_salary = (
            total_sum / len(salaries) if salaries and len(salaries) else 0.0
        )
        return (total_sum, average_salary)

    return handle_file(
        path,
        file_handler,
        error_value=(0.0, 0.0),
    )
