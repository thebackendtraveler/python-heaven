#importing the os module, and then removing a file
import os
os.remove("test_file.txt")

#checking if the file exists, and then removing it
if os.path.exists("test_file.txt"):
    os.remove("test_file.txt")
else: 
    print("This file does not exist. Please try again")

#removing a folder
os.rmdir("myfolder")

#create a new file, writing to it and then closing
f = open("test_file.txt", "x")
f.write("This is a new line")
f.close()

#Opening the file in write mode and overwriting its contents
f = open("test_file.txt", "w")
f.write("The content of the file will be overwritten")
f.close()

#opening the file in append mode, and adding a new line to the file
f = open("test_file.txt", "a")
f.write("This sentence is going to be added in the end of the file")
f.close()

#opening the file and reading from it
f = open("test_file.txt", "r")
print(f.read())

#to open the file in read mode and as text value
f = open("test_file.txt", "rt")

#to open the file in read mode and as binary value
f = open("test_file.txt", "rb")

#to open a file on a different location, we use the file path
f = open("C:\\tmp\welcome.txt", "r")
print(f.read())

#to only read the 5 first characters of the file
f = open("test_file.txt", "r")
print(f.read(5))

#to read one line of the file
f = open("test_file.txt", "r")
print(f.readline())

#to read two lines of the file
f = open("test_file.txt", "r")
print(f.readline())
print(f.readline())

#to loop through the file line by line
f = open("test_file.txt", "r")
for x in f:
    print(x)