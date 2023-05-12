class TwoDimensionalShape:
    class Rectangle:
        def __init__(self, length, width, display_character):
            self.length = length
            self.width = width
            self.display_character = display_character
    
        def calculate_area(self):
            return self.length * self.width
    
        def display(self):
            print("Rectangle (1 x w): {0} x {1} with area {2}".format(self.length, self.width, self.calculate_area()))
        
            print()
            for current in range (0, self.width):
                print(self.display_character * self.length)
            
    class Square:
        def __init__(self, length, width, display_character):
            self.length = length
            self.width = length
            self.disply_character = display_character
    
        def calculate_area(self):
            return self.length * self.width
    
        def display(self):
            print("Square (1 x w): {0} x {1} with area {2}".format(self.length, self.width, self.calculate_area()))
        
            print()
            for current in range(0, self.width):
                print(self.display_character * self.length)