#!python3

class Student:
    count = 0

    def __init__(self):
        self.name = "" # Assign to an instance variable
        self.surname = "" # Assign to an instance variable
        Student.count += 1 # Assign to the class variable
        self.number = Student.count # Assign to an instance variable

first_student = Student() # no arguments are passed, self is implicit
first_student.name = "John"
first_student.surname = "Doe"

second_student = Student()
second_student.name = "Jane"
second_student.surname = "Doe"

print("{}: {} {}".format(first_student.number ,first_student.name,first_student.surname))
print("{}: {} {}".format(second_student.number,second_student.name,second_student.surname))
print("Number of students:  {}".format(Student.count))

