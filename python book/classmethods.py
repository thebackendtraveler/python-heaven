#!python3

class Student:
    count = 0

    def __init__(self, name, surname):
        self.name = name # Assign the received parameter's value
        self.surname = surname # Assign the received parameter's value
        Student.count += 1
        self.number = Student.count
        self.grades = {} # Subjects and their results (empty)

    def display(self):
        print("{}:\t{} {}".format(self.number ,self.name,self.surname))
        print()
        if len(self.grades) == 0:
            print("\tNo subjects and results have been added")
        else:
            for key in self.grades:
                print("\t{}:\t\t{}".format(key,self.grades[key]))

            # Use self to call the calculate_average method
            print("\tAverage:\t{}".format(self.calculate_average()))

        print("-" * 50)

    def add_subject_and_mark(self,subject,mark):
        self.grades[subject] = mark

    def calculate_average(self):
        total = 0

        for key in self.grades:
            total += self.grades[key]

        return total / len(self.grades)

first_student = Student("John","Doe") # Name and surname passed as arguments
second_student = Student("Jane","Doe")
# Add 2 subjects and marks to the second student
second_student.add_subject_and_mark("NET",75)
second_student.add_subject_and_mark("PRG",90)

# Display the results of both students
first_student.display()
second_student.display()

print("Number of students:  {}".format(Student.count))

