import os
import pathlib

# import file format dictionary from ressources.py
from ressources import fileFormat

# path to dowloads folder of current OS user
path = pathlib.Path.home() / "Downloads"

fileTypes = list(fileFormat.keys())
fileFormats = list(fileFormat.values())

def main():
	if not os.path.exists(path) or not os.path.isdir(path):
		print("Path is invalid")
		return
	
	setting = input("Do you want to automatically sort your files? (y/n) > ")
	
	if setting.lower() == "y":
		for file in os.scandir(path):
			if not file.is_file():
				continue
				
			fileName = file.name
			fileFormatType = "." + fileName.split(".")[-1]
			
			if setting == "y":
				for i in range(len(fileFormats)):
					if fileFormatType in fileFormats[i]:
						print(f"...File {fileName} moved to {fileTypes[i]} folder")
						folder = path / fileTypes[i]
						if not os.path.exists(folder):
							os.mkdir(folder)
						os.rename(path / fileName, folder / fileName)
						break
				else:
					print(f"No file format found for {fileName}")
					folder = path  / "Other"
					if not os.path.exists(folder):
							os.mkdir(folder)
					os.rename(path / fileName, folder / fileName)
					break

	elif setting == "n":
		# your code for manual cleanup goes here
		pass

if __name__ == "__main__":
	main()