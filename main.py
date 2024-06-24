import os
import logging
from pathlib import Path
from ressources import FILE_FORMAT_FOLDERS
import time


PATH: Path = Path.home() / "Downloads"  # Path to the folder you want to sort
FILEFORMATS = list(FILE_FORMAT_FOLDERS.keys())  # List of file formats
FILETYPES = list(FILE_FORMAT_FOLDERS.values())  # List of file types
LOGFILE = Path("logs/file_sorter.log")  # Path to the log file

# Create the log file if it doesn't exist
if not LOGFILE.exists():
    LOGFILE.touch()

# Set up logging
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


def autoSort(file: Path) -> None:
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


def main():
    if invalidPath():
        logging.error("Path is invalid")
        return

    setting = (
        input("Do you want to automatically sort your files? (Y/n) > ").lower() or "y"
    )

    match (setting):
        case "y":
            for file in PATH.iterdir():
                if isNotaFile(file):
                    continue

                autoSort(file)
        case "n":
            logging.info("Start iterating manually")

            pass

        case _:
            logging.error(f"Invalid Input: {setting}")
            return


if __name__ == "__main__":
    main()
