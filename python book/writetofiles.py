#!python3

print("Opening thefile.txt")
# Opens "thefile.txt" in writable mode
# If the file doesn't exist, it is created
my_file = open("thefile.txt","w")
print()
print("File methods and properties:")
# The name property provides the file system name of the associated file
print("name: ", my_file.name)
# The mode property provides details on which mode the file was opened as
print("mode: ", my_file.mode)
# The closed property returns true if the file is closed
print("closed: ", my_file.closed)
# The readable() method returns true if the file is readable
print("readable(): ", my_file.readable())
# The writable() method returns true if the file is writable
print("writable(): ", my_file.writable())
print()
print("Opening thefile.txt")
# Closes the file to release the resources
my_file.close()
print()
print("File methods and properties:")
print("closed: ", my_file.closed)

my_file = open("thefile.txt","w")

# The \n escape character signifies new lines.
# The following string will be written to file
# as 3 separate lines.
write_me = "These lines\nwill be written\nto file.\n"
my_file.write(write_me)

# Lines may also be written one at a time, by calling
# write() for each line to be written.  
my_file.write("Extra line 1\n")
my_file.write("Extra line 2\n")
my_file.write("Extra line 3\n")

my_file.close()


my_file = open("thecsvfile.csv","w")

# First row / heading
my_file.write("Name,Description,Amount\n")
# Other rows
my_file.write("John Doe, First customer, 1000.00\n")
my_file.write("Jane Doe, Second customer, 2500.00\n")

my_file.close()

