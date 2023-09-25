import os
import pathlib

# import file format dictionary from ressources.py
from ressources import fileFormat

# path to dowloads folder of current OS user
path = pathlib.Path.home() / "Downloads"

fileTypes = list(fileFormat.keys())
fileFormats = list(fileFormat.values())

def manual_cleanup():
    if not os.path.exists(path) or not os.path.isdir(path):
        print("Path is invalid")
        return
        
    for file in os.scandir(path):
        if not file.is_file():
            continue
        
        fileName = file.name
        fileFormatType = "." + fileName.split(".")[-1]
        
        print(f"File name: {fileName} \nFile path: {path} \nFile size: {file.stat().st_size} bytes")
        print(fileFormatType)
        
manual_cleanup()