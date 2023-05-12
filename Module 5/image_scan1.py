from PIL import Image
import imagehash
import os
import glob

#Please ensure to enter a full filepath to the folder
scan_folder = input("Please enter the folder of images to be scanned: ")
filename = input("Please mention the file and filepath to save results in: ")
results = ""

os.chdir(scan_folder)

image_file_to_match_hash = ""

for image_file_to_match in glob.glob("*.jpg"):
    image_file_to_match_hash = imagehash.average_hash(
        Image.open(image_file_to_match))
    print("Finding a match for {0}".format(image_file_to_match))
    
    for image_scan in glob.glob("*.jpg"):
        if image_file_to_match != image_scan: 
            image_scan_hash = imagehash.average_hash(
                (Image.open(image_scan)))
            
            if image_file_to_match == image_scan_hash:
                results = results + \
                    "{0},{1},{2}\n".format(
                        image_scan, image_scan_hash, image_file_to_match)

print("The scan has been completed...")
print("*" * 50)
print("Saving results to {}".format(filename))
f = open((filename), "w")
f.write("Matched fimage files found\n")
f.write("filename, hash, match file\n")
f.write(results)
f.close()