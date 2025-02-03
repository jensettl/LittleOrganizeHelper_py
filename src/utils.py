import os
from pathlib import Path
from ressources.file_formats import FILE_FORMAT_FOLDERS
import logging
import time

USER = os.getlogin()
FOLDER = "Downloads"
FOLDER_PATH = Path(f"C:/Users/{USER}/{FOLDER}")  # Path to the folder to be sorted

def invalidPath(path: Path) -> bool:
    """Checks if the path is invalid."""
    return not path.exists() or not path.is_dir()

def isNotaFile(file: Path) -> bool:
    """Checks if the file is not a file."""
    return not file.is_file()
  
def printFile(file: Path) -> None:
  """Prints the file name, file format, and file size."""
  file_info = f"File: {file.name} | File format: {file.suffix} | File size: {round(file.stat().st_size/1000000,2)} Megabytes"
  hLine = len(file_info) * "-"
  print(f"{hLine}\n{file_info}\n{hLine}")

def autoSort(file) -> None:
    """Automatically sorts a file into the appropriate folder based on its file format."""
    format_type: str = file.suffix.lower() 

    if format_type in FILE_FORMAT_FOLDERS:
        folder_name: str = FILE_FORMAT_FOLDERS[format_type]
        folder_path: Path = file.parent / folder_name

        if invalidPath(folder_path):
            logging.error(f"Path {folder_path} does not exist. Creating the folder...")
            folder_path.mkdir()

        try:
            logging.info(f"Moving {file.name} to {folder_name} folder")
            file.rename(folder_path / file.name)
            time.sleep(0.3)
        except FileExistsError:
            logging.error(f"File {file.name} already exists in {folder_name} folder")
    else:
        logging.info(f"No file format found for {file.name}. Moving to 'Other' folder")
        other_folder_path: Path = file.parent / "Other"

        if not other_folder_path.exists():
            other_folder_path.mkdir()

        try:
            file.rename(other_folder_path / file.name)
            time.sleep(0.3)
        except FileExistsError:
            logging.error(f"File {file.name} already exists in 'Other' folder")

    print("-" * 50)


def manualSort(file) -> None:
    """Manually sorts all files of a folder into the appropriate folder based on user input."""
    
    printFile(file)
    setting = input(
        "(1) Move automatically, (2) Delete, (3) Skip or (4) Custom Path. > "
    )

    match (setting):
        case "1":
            autoSort(file)
        case "2":
            logging.info(f"Deleted {file.name} from {file.parent} folder")
            os.remove(FOLDER_PATH / file)
        case "3":
            logging.info(f"Skipped {file.name} from {file.parent} folder")
        case "4":
            customPath = input("Enter the custom path > ")
            if invalidPath(Path(customPath)):
                logging.error(f"Path {customPath} does not exist")
            logging.info(f"Moving {file.name} to {customPath} folder")
            file.rename(Path(customPath) / file.name)
        case "q":
            logging.info("Quitting the program")
        case _:
            logging.error(f"Invalid Input: {setting}")