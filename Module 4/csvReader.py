#make sure to have a csv file before running this script
#Include the filepath in the my_file below

#This code is for opening the csv file
my_file = open('c:\\MyScripts\Module 4\mycsv.csv', 'r')
#This print statement will print the content of the csv file to the terminal
print(my_file.read())

#This for loop will go through each lines of the csv file 
for line in my_file:
    print(line, end ="")

#This code will close the file
my_file.close()