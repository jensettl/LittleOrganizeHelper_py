import os

with open("folder_organizer.bat", "w") as f:
    # get current working directory and write it to the bat file
    current_working_directory = os.getcwd()
    
    # check if its a windows system
    if os.name == "nt":
        current_working_directory = current_working_directory.replace("\\", "/")
    
    f.write(
        f"""
@echo off
"C:/Users/Jens/anaconda3/python.exe" "{current_working_directory}/folderOrganizer.py"
pause
"""
    )