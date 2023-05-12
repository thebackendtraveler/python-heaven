from PIL import Image
import imagehash
import os
import glob

hash = imagehash.average_hash(Image.open('image2.jpg'))
print(hash)
otherhash = imagehash.average_hash(Image.open('image3.jpg'))
print(otherhash)
print(hash == otherhash)


hash2 = imagehash.average_hash(Image.open('image1.jpg'))
print(hash2)
otherhash2 = imagehash.average_hash(Image.open('image2.jpg'))
print(otherhash2)
print(hash2 == otherhash)

os.chdir("./C://MyScripts/Module 5/Tasks/ Lesson")

image_file_to_match_hash = ""

print("Scanning started...")

for image_file_to_match in glob.glob("*.jpg"):
  image_file_to_match_hash = imagehash.average_hash( Image.open(image_file_to_match))
print("Finding a match for {0}".format(image_file_to_match))

for image_scan in glob.glob("*.jpg"):
    if image_file_to_match != image_scan:
        image_scan_hash = imagehash.average_hash((Image.open(image_scan)))

        if image_file_to_match_hash == image_scan_hash:
                print("Match found with {0}".format(image_scan))