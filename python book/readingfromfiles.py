#!python3

# The file is opened using the readable mode
my_file = open("thefile.txt","r")

# Display all the contents of the file
print(my_file.read())

# Display all the contents of the file again
# The individual lines in a file may be processed 
# using a for loop.
for line in my_file:
    # Suppress the new line at the end of the line,
    # since the line of text read from the file already
    # contains a newline character at the end.
    print(line, end="")
    
my_file.close()


# The file is opened using the readable mode
my_file = open("thefile.txt","r")

# Display all the contents of the file
print(my_file.read())
print("Position {}".format(my_file.tell()))
print("Resetting position to 50")
my_file.seek(50)
print("Position {}".format(my_file.tell()))
print()
# Display all the contents of the file again, but
# starting from position 50.  That means only a 
# portion of the file will be read.
for line in my_file:
    # Suppress the new line at the end of the line,
    # since the line of text read from the file already
    # contains a newline character at the end.
    print(line, end="")
    
my_file.close()

# The file is opened using the readable mode
my_file = open("thecsvfile.csv","r")

# readline is used to read all of a file's contents at once
file_contents = my_file.readlines()
print(file_contents)
print()
# The individual lines are stored as elements in a string-based list
for line in file_contents:
    print(line,end="")

my_file.close()

