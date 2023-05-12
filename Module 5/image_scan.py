# If the required modules are not installed they can be installed with
#  pip install imagehash
# pip install pillow

# Import the required files
from PIL import Image
import imagehash
import os
import glob

# Ask the end user which folder must be scanned with images in
# The folder to scan must have two pictures that are the same, and 
# you must create a folder to be scanned before running the script
scan_folder = input("Please enter the filepath of the folder to be scanned: ")
# Ask the user what the filename should be to save the results in
# Enter a full filepath with a filename.txt at the end
filename = input("Please enter the filename and filepath to save the results in: ")
# Variable to save the matched results in
results = ""

# Change the directory to the folder the the user provided to scan
os.chdir(scan_folder)

#This code is to match an existing file hash with a hash from an unknown file in the folder
image_file_to_match_hash = ""

print("Scanning started...")

# Get all the files in the folder that has a .jpg extension
for image_file_to_match in glob.glob("*.jpg"):
    image_file_to_match_hash = imagehash.average_hash(
        Image.open(image_file_to_match))
    print("Finding a match for {0}".format(image_file_to_match))

    for image_scan in glob.glob("*.jpg"):
        if image_file_to_match != image_scan:
            image_scan_hash = imagehash.average_hash(
                (Image.open(image_scan)))

            if image_file_to_match_hash == image_scan_hash:
                results = results + \
                    "{0},{1},{2}\n".format(
                        image_scan, image_scan_hash, image_file_to_match)

# Print the results to the user
print("Done with the scan")
print("*" * 50)
print("Saving results to {}".format(filename))
# Save the resuls to the provided filename.
f = open((filename), "w")
f.write("Matched fimage files found\n")
f.write("filename,hash, match file\n")
f.write(results)
f.close()
