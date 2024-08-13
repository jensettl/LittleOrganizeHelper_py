# OrganizeHelper

## Description

The **OrganizeHelper** is a Python script that automatically sorts files into different folders based on their file format. The script uses the _Downloads folder_ by default (this can be adjusted by changing the _PATH_ Variable) then gives the user the option to automatically sort their files or manually sort them.

## How it works

The script defines a dictionary called `FILE_FORMAT_FOLDERS` in `file_formats.py` that maps each valid file format to its corresponding folder. When the user chooses to automatically sort their files, the script iterates through each file in the directory and checks its file format against the `FILE_FORMAT_FOLDERS` dictionary. If the file format is found in the dictionary, the script moves the file to the corresponding folder. If the file format is not found in the dictionary, the script moves the file to the "Other" folder.

```python
# Get the file format of the file and determine destination folder
folder_name: str = FILE_FORMAT_FOLDERS[format_type]
folder_path: Path = file.parent / folder_name

# Move the file to the corresponding folder
file.rename(folder_path / file.name)
```

## Requirements

- Python 3.10 or higher
- pathlib module
- logging module

## Usage

1. Clone the repository to your local machine.
2. Adjust the `PATH` variable in `folderOrganizer.py` to the path of the directory you want to sort.
   2.1. Add any file formats you want to sort to the `FILE_FORMAT_FOLDERS` dictionary in `ressources.py`.
3. Run the script using Python 3.10 or higher.
4. Choose in the `console` if you want to automatically sort the files or manually sort them.

## Early Development Version

This script is still in the early stages of development and may contain bugs or issues. Please use it with caution and report any problems you encounter.

## Additional Information

Tested on Windows 10 with Python 3.10.0
