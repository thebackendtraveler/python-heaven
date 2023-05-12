#!python3

class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Frey")

for attribute in dir(first):
    print(attribute)

for key in first.__dict__:
    print("{}:\t{}".format(key,first.__dict__[key]))