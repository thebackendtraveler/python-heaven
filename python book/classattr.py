#!python3

class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Freya")
second = Employee("Klaus")
del second.name

print(first.name)
print(second.name)

class Employee:
    def __init__(self, name):
        self.name = name

first = Employee("Frey")
second = Employee("Klaus")

# Set the attribute "name" of first to "Freya"
setattr(first,"name","Freya")
# Get the attribute "name" of first
print(getattr(first,"name"))

# Delete the attribute "name" of second
delattr(second,"name")

# Test if second has the attribute "name"
if hasattr(second,"name"):
    print(getattr(second,"name"))
else:
    print("second does not have attribute name")

