from random import random

output = ""

for current in range(0, 100):
    print(current)
    output += str (int(random() * 500)) + ","


print("The output from the loop: ", output)

user_file = input("Please provide a file name: ")
my_file = open(user_file, "w")
my_file.write(output)
my_file.close()