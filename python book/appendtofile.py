#!python3

# The file is opened using the readable mode
my_file = open("thefile.txt","a")

for i in range(0,4):
    # The write statement appends an extra line to the file.
    my_file.write("Another line {}\n".format(i + 1))

my_file.close()

