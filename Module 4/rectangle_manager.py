from rectangle import *

rectangles = list()

user_input = 'y'

while user_input == 'y':
    print("Please enter details of a rectangle: ")
    length = int(input("Length: "))
    width = int(input("Width: "))
    display_char = input("Display Character: ")

    rec = Rectangle(length, width, display_char)
    rectangles.append(rec)
    user_input = input("Would you like to create another rectangle? ( y or n)")
    print("-" * 70)

for current in rectangles:
    current.display()
    print()