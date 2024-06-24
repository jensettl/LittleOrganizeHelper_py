import os
import logging
from pathlib import Path
from ressources import FILE_FORMAT_FOLDERS
import time


PATH: Path = Path.home() / "Downloads"  # Path to the folder you want to sort
FILEFORMATS = list(FILE_FORMAT_FOLDERS.keys())  # List of file formats
FILETYPES = list(FILE_FORMAT_FOLDERS.values())  # List of file types
LOGFILE = Path("logs/file_sorter.log")  # Path to the log file

if not LOGFILE.exists():
    LOGFILE.touch()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/file_sorter.log"), logging.StreamHandler()],
)


def invalidPath() -> bool:
    """Checks if the path is invalid."""
    return not PATH.exists() or not PATH.is_dir()


def isNotaFile(file: Path) -> bool:
    """Checks if the file is not a file."""
    return not file.is_file()


def printFile(file: Path) -> None:
    """Prints the file name, file format, and file size."""
    file_info = f"File: {file.name} | File format: {file.suffix} | File size: {round(file.stat().st_size/1000000,2)} Megabytes"
    hLine = len(file_info) * "-"
    print(f"{hLine}\n{file_info}\n{hLine}")


def autoSort(file) -> None:
    """Automatically sorts all files of a folder into the appropriate folder based on its file format."""
    format_type: str = file.suffix.lower()

    if format_type in FILE_FORMAT_FOLDERS:
        folder_name: str = FILE_FORMAT_FOLDERS[format_type]
        folder_path: Path = file.parent / folder_name

        if not folder_path.exists():
            folder_path.mkdir()

        try:
            logging.info(f"Moving {file.name} to {folder_name} folder")
            file.rename(folder_path / file.name)
            time.sleep(0.2)
        except FileExistsError:
            logging.error(f"File {file.name} already exists in {folder_name} folder")
    else:
        logging.info(f"No file format found for {file.name}. Moving to 'Other' folder")
        other_folder_path: Path = file.parent / "Other"

        if not other_folder_path.exists():
            other_folder_path.mkdir()

        try:
            file.rename(other_folder_path / file.name)
        except FileExistsError:
            logging.error(f"File {file.name} already exists in 'Other' folder")


def manualSort(path: Path) -> None:
    """Manually sorts all files of a folder into the appropriate folder based on user input."""
    for file in path.iterdir():
        if isNotaFile(file):
            continue

        printFile(file)

        setting = input(
            "(1) Move automatically, (2) Delete, (3) Skip or (4) Custom Path. Press 'q' to quit) > "
        )

        match (setting):
            case "1":
                autoSort(file)
            case "2":
                logging.info(f"Deleted {file.name} from {file.parent} folder")
                os.remove(PATH / file)
            case "3":
                logging.info(f"Skipped {file.name} from {file.parent} folder")
                continue
            case "4":
                customPath = input("Enter the custom path > ")
                if not Path(customPath).exists():
                    logging.error(f"Path {customPath} does not exist")
                    break

                logging.info(f"Moving {file.name} to {customPath} folder")
                file.rename(Path(customPath) / file.name)
            case "q":
                logging.info("Quitting the program")
                break
            case _:
                logging.error(f"Invalid Input: {setting}")
                break


def main():
    if invalidPath():
        logging.error("PATH Variable is invalid")
        return

    setting = (
        input("Do you want to automatically sort your files? (Y/n) > ").lower() or "y"
    )

    match (setting):
        case "y":
            logging.info("Start iterating automatically\n")
            for file in PATH.iterdir():
                if isNotaFile(file):
                    continue
                autoSort(file)

        case "n":
            logging.info("Start iterating manually\n")

            manualSort(PATH)

        case _:
            logging.error(f"Invalid Input: {setting}")
            return


if __name__ == "__main__":
    main()
