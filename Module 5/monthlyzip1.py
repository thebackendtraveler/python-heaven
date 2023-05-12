import zipfile
import os
from pathlib import Path
import shutil
from datetime import datetime

#Asking the user for a new directory name
new_directory = input("Enter the name of the new directory: ")

#Checking if the specified directory exists, if not we create it
if not os.path.exists(new_directory):
    os.mkdir(new_directory)

#Asking the user for the source folder to copy files into
entries = Path(input("Please input a path to copy: "))

#Scanning the source folder to get all the files in it
for entry in entries.iterdir():
    filename = os.path.basename(entry)
    shutil.copy(entry, new_directory + "/" + filename)
    results = os.stat(entry)
    filename_parts = filename.split(".")
    #Giving the destination file a new datetime stamp
    creation_time = datetime.fromtimestamp(results.st_ctime).date()
    new_filename = "{0} {1}.{2}".format(
        filename_parts[0], creation_time, filename_parts[1])
    os.rename(new_directory + "/" + filename,
              new_directory + "/" + new_filename,)
    
entries = Path(new_directory)

#Showing the user all the files that has been copied
for entry in entries.iterdir():
    print(entry)

#Zip the files in the folder and give the filename a date and time of now
zipfile_name = "{0}.zip".format(datetime.now().date())

with zipfile.ZipFile(zipfile_name, "w") as zipfile:
    for source in entries.iterdir():
        zipfile.write(source)