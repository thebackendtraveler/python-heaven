#!python3

class Student:
    count = 0   # A count of the number of students, initialized to 0

from Student import *

# Creates a Student object and increments its count
first_student = Student()
Student.count += 1
# Creates another Student object and increments its count
second_student = Student()
Student.count += 1

# Demonstrates that the value of count is shared amongst
# all Student instances
print("Number of students:  {}".format(Student.count))

