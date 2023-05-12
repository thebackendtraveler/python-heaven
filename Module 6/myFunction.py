def calculate_area(name):
    name = name.lower()
    if name == "rectangle":
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: "))
        rect_area = l * b
        print(f"The area of rectangle is {rect_area}.")
 
