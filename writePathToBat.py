import os

with open("folder_organizer.bat", "w") as f:
    # get current working directory and write it to the bat file
    current_working_directory = os.getcwd()
    
    # python installation path
    python_path = "C:/Users/Jens/anaconda3/python.exe"
    
    # check if its a windows system
    if os.name == "nt":
        current_working_directory = current_working_directory.replace("\\", "/")
        python_path = python_path.replace("\\", "/")
    
    f.write(
        f"""
@echo off
"{python_path}" "{current_working_directory}/folderOrganizer.py"
pause
"""
    )