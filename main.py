import logging
from pathlib import Path
from ressources.file_formats import FILE_FORMAT_FOLDERS
from src.utils import invalidPath, isNotaFile, autoSort, manualSort, FOLDER_PATH, FOLDER
from tqdm import tqdm

LOGFILE = Path(f"logs/folder_cleanup_{FOLDER}.log")  # Path to the log file

if not LOGFILE.parent.exists():
    LOGFILE.parent.mkdir(parents=True)
if not LOGFILE.exists():
    LOGFILE.touch()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/file_sorter.log"), logging.StreamHandler()],
)

def main():    
    if invalidPath(FOLDER_PATH):
        logging.error("FOLDER_PATH Variable is invalid")
        return

    setting = (
        input("Do you want to automatically sort your files? (Y/n) > ").lower() or "y"
    )

    files = [file for file in FOLDER_PATH.iterdir() if not isNotaFile(file)]
    total_files = len(files)

    match (setting):
        case "y":
            logging.info("Start iterating automatically\n")
            for file in tqdm(files, total=total_files, desc="Sorting files"):
                print("")
                autoSort(file)
                print("")
        case "n":
            logging.info("Start iterating manually\n")
            for file in tqdm(files, total=total_files, desc="Sorting files"):
                manualSort(file)
        case _:
            logging.error(f"Invalid Input: {setting}")
            return

if __name__ == "__main__":
    main()
