# LittleOrganizeHelper_py

The **OrganizeHelper** is a Python script that automatically sorts files into different folders based on their file format. The script uses the _Downloads folder_ by default (this can be adjusted by changing the _PATH_ Variable) then gives the user the option to automatically sort their files or manually sort them.

### How it works

The script defines a dictionary called `FILE_FORMAT_FOLDERS` in `ressources.py` that maps each valid file format to its corresponding folder. When the user chooses to automatically sort their files, the script iterates through each file in the directory and checks its file format against the `FILE_FORMAT_FOLDERS ` dictionary. If the file format is found in the dictionary, the script moves the file to the corresponding folder. If the file format is not found in the dictionary, the script moves the file to the "Other" folder.

### Requirements

- Python 3.x
- pathlib module
- logging module

### Usage

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the directory containing the main.py file.
3. Adjust the `PATH` variable in `main.py` to the path of the directory you want to sort.
4. Add any file formats you want to sort to the `FILE_FORMAT_FOLDERS` dictionary in `ressources.py`.
5. Choose whether you want to automatically sort your files or manually sort them by following the prompts in the terminal.

### Additional Information

Tested on Windows 10
