# some more tips:
# let's create an "enum" style dictionary to make our options more readable:
class Iota:
    def __init__(self, start = 0):
        self._value = start
    
    @property
    def value(self) -> int:
        oldValue = self._value
        self._value += 1
        return oldValue
    
    @value.setter
    def value(self, v):
        self._value = v

iota :Iota = Iota(1) # don't worry about this, it might be a bit complicated

OPTIONS = { # this is our enum
    "SQUARE"    : iota.value, # 1
    "RECTANGLE" : iota.value, # 2
    "CIRCLE"    : iota.value, # 3
    "CUBE"      : iota.value, # 4
    "CYLINDER"  : iota.value, # 5
    "EXIT"      : 6,
}

def get_rectangle_area(width : int = 0, height : int = 0): return width * height
# squares are just special rectangles, this helper function helps us to not repeat code

def main_menu2():
    print("Welcome!")
    option = 1
    while option != OPTIONS["EXIT"]:
        print(
            "1. Square",
            "2. Rectangle",
            "3. Circle",
            "4. Cube",
            "5. Cylinder",
            ("-" * 80),
            "6. Exit the program",
            sep = "\n"
        ) # the less function calls the better!
        
        option = int(input("Please select an option from the menu above (1-6): "))

        if option == OPTIONS["SQUARE"]: # more readable?
            width = int(input("Enter a width for the square: "))
            print("The area of your square is", get_rectangle_area(width, width))
        
        if option == OPTIONS["RECTANGLE"]:
            width = int(input("Enter a width for the rectangle: "))
            height = int(input("Enter a height for the rectangle: "))
            print("The area of your rectangle is", get_rectangle_area(width, height))

        if option <= 0 or option > 6: print("Invalid option")
        elif option > 2 and option != 6: print("Not implemented")

        print("")
    
    print("Thanks for playing!")

main_menu2()