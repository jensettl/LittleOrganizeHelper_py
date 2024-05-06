import os
import logging
from pathlib import Path
from ressources import FILE_FORMAT_FOLDERS

# path to downloads folder of current OS user
PATH: Path = Path.home() / "Downloads"
fileFormats = list(FILE_FORMAT_FOLDERS.keys())
fileTypes = list(FILE_FORMAT_FOLDERS.values())

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/file_sorter.log"), logging.StreamHandler()],
)


def autoSort(file: Path) -> None:
    """Automatically sorts a file into the appropriate folder based on its file format."""
    file_format_type: str = file.suffix.lower()

    if file_format_type in FILE_FORMAT_FOLDERS:
        folder_name: str = FILE_FORMAT_FOLDERS[file_format_type]
        folder_path: Path = file.parent / folder_name

        if not folder_path.exists():
            folder_path.mkdir()

        logging.info(f"Moving {file.name} to {folder_name} folder")
        file.rename(folder_path / file.name)
    else:
        logging.info(f"No file format found for {file.name}. Moving to 'Other' folder")
        other_folder_path: Path = file.parent / "Other"

        if not other_folder_path.exists():
            other_folder_path.mkdir()

        file.rename(other_folder_path / file.name)


def main():
    if not PATH.exists() or not PATH.is_dir():
        logging.error("Path is invalid")
        return

    # setting = input("Do you want to automatically sort your files? (Y/n) > ")
    setting = "y"

    # Automatically sort files
    if setting.lower() == "y":
        # Iterate through files and automatically move them to the right folder
        for file in PATH.iterdir():
            if not file.is_file():
                continue

            autoSort(file)

    # Manually sort files
    elif setting.lower() == "n":
        logging.info("Start iterating manually")

        for file in PATH.iterdir():
            if not file.is_file():
                continue

            print(
                f"File: {file.name} | File format: {file.suffix} | File size: {round(file.stat().st_size/1000000,2)} Megabytes"
            )

            action = input(
                "What do you want to do with this file? (1) Move automatically, (2) Delete or (3) Skip) > "
            )
            print("")

            if action == "1":
                autoSort(file)
            elif action == "2":
                logging.info(f"Deleted {file.name} from {file.parent} folder")
                print(f"...File {file} deleted\n")
                os.remove(PATH / file)
            elif action == "3":
                logging.info(f"Skipped {file.name} from {file.parent} folder")
                print(f"...File {file} skipped\n")
                continue
            else:
                logging.error(f"Invalid Input: {action}")
                break


if __name__ == "__main__":
    main()
