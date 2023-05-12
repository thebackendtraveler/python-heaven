class ThreeDimensionalShape: 
    class Cube:
        def __init__(self, length, width, height, display_character):
            self.length = length
            self.width = width 
            self.height = height
            self.display_character = display_character
        
        def calculate_area(self):
            return self.length * self.width * self.height
    
        def display(self):
            print("Cube (1 x w): {0} x {1} x {2} with area {3}".format(self.length, self.width, self.calculate_area()))
        
            print()
            for current in range(0, self.width):
                print(self.display_character * self.length)
                
    class Box:
        def __init__(self, length, width, height, display_character):
            self.length = length 
            self.width = width 
            self.height = height
            self.display_character = display_character 
        
        def calculate_area(self):
            return self.length * self.width * self.height
    
        def display(self):
            print("Box (1 x w): {0} x {1} x {2} with area {3}".format(self.length, self.width, self.height, self.calculate_area()))
        
            print()
            for current in range(0, self.width):
                print(self.display_character * self.length)