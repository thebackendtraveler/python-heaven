def main_menu(length = 0, height = 0, width = 0, radius = 0): # why parameters here?
    # if you want to create local variables to your functions you can do so like with any other variable,
    # passing parameters u never use to your functions serves no purpose and risks being quite confusing..
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Cube")
    print("5. Cylinder")
    print("-" * 80)
    print("6. Exit the program")

    option = 0 # why set it to 0 and then reset it immediately? this would make sense if the input selection
    # was inside the while loop
    option = int(input("Please select an option from the menu above: "))
    while option != 6: # think about it: how many times does this while loop run?
        if option == 1:
            length = int(input("Enter a length for the square: "))
            square_area = length * length # ok, but you could use length ** 2
            print("The area of your square is", (square_area))
            main_menu() # here lies the problem: most languages, python included, keep track of all the
            # functions you call at runtime in a structure called "call-stack", basically a list where
            # all the names of the functions you call get added to, and removed once you return from them.
            # let's see what happens at runtime:
            # 1) main_menu is called, the menu is printed and you select your option. The call stack: [main_menu]
            # 2.1) if your option == 6, the while loop doesn't run and main_menu returns. The call stack: []
            # 2.2) otherwise, the while loop runs and an option is selected.
            # 3) once the area is calculated, you call main_menu again!!!. The call stack: [main_menu, main_menu]
            # 4) if you keep using the program, the call stack fills up with unresolved calls to main_menu
            # 5) eventually, the call stack runs out of memory and you get a Stack Overflow Error (this is bad!)
            # this "build up" of function calls happens often in recursive programs when an edge case is overlooked,
            # here u don't need to make it recursive at all
        
        if option == 2:
            length = int(input("Enter a length for the rectangle: "))
            width = int(input("Enter a height for the rectangle: "))
            rect_area = length * height
            print("The area of your rectangle is", (rect_area))
            main_menu()
        
        if option > 2:
            print("Not implemented...")
            main_menu()

# how do we solve this? Notice how the while loop runs either 0 or 1 times, so it's not a loop, it's an if statement
# to make it useful, we need to put the option selection INSIDE of the while loop:
# pseudo-code:
# while option != 6:
#   print the menu
#   select the option
#   if option == 1:
#       get square info
#       calculate square area
#       print area

#   if option == 2:
#       get rect ingo
#       calculate rect area
#       print area
#   ...
#   if option < 0 or option > 7: print("The option is invalid")

#let's try:
def main_menu2(): # no parameters needed
    option = 1 # any random value that the while loop will accept is good, we just need to get inside it
    while option != 6:
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Cube")
        print("5. Cylinder")
        print("-" * 80)
        print("6. Exit the program") # maybe you don't want to take up so much space, you could have the menu
                                     # print only once by moving it out the loop
        option = int(input("Please select an option from the menu above (1-6): "))

        if option == 1:
            width = int(input("Enter a width for the square: "))
            print("The area of your square is", (width ** 2))
        
        if option == 2:
            width = int(input("Enter a width for the rectangle: "))
            height = int(input("Enter a height for the rectangle: "))
            print("The area of your rectangle is", (width * height))

        if option < 0 or option > 6: print("Invalid option")
        elif option > 2 and option != 6: print("Not implemented")

        print("") # let's space things out a bit :)
    
    print("Thanks for playing!") # we get here only if option == 6

main_menu2()