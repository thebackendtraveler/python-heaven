
def main_menu():
    #This is the main menu for converting inches to centimeters
    print("1. Convert centimeters to inches: ")
    print("2. Convert inches to centimeters: ")
    print("-"*80)
    print("3. Exit the program")
    #Asking the user to choose an option, where option one is converting centimeters, and option 2 is converting inches 
    option = int(input("Please select an option from the list above: "))
    while option != 3:
        #This is a while loop, that will continue forever until its criterias has been met. 
        # Which is why we set it to != (the not operator) 3. This means that the code will run 
        # as long as the user does not select 3 
        if option == 1:
            # If the user selects option 1, run the code to convert centimeters to inches
            #Asking the user for centimters to convert to inches
            centimeters = int(input("Convert centimeters to inches, please enter centimeters to convert: "))
            #This is the code that will convert centimeters to inches
            inches = centimeters / 2.54
            print("-"*80)
            print("$"*80)
            #This print statement will print the centimeters, from the user on the left side, and the inches on the right side
            print("Centimeters: {0} Inches: {1}".format(str(centimeters).ljust(20, " "), str(inches).rjust(5, " ")))
            print("$"*80)
            print("-"*80)
            #Navigating back to the main_menu and stopping the above print statement from executing in a loop
            main_menu()
        if option == 2:
            # If the user selects option 2, run the code to convert inchesd to centimeters
            #Asking the user for centimeters to convert
            inches = int(input("Convert inches to centimeters, please enter inches to convert: "))
            #this is the code that will convert inches to centimeters
            centimeters = inches * 2.54
            print("-"*80)
            print("£"*80)
            #This print statement will print ther inches from the user on the left side, and the centimeters on the right side
            print("Inches: {0} Centimeters: {1}".format(str(inches).ljust(20, " "), str(centimeters).rjust(5, " ")))
            print("£"*80)
            print("-"*80)
            #Navigating back to the main_menu and stopping the above print statement from executing in a loop
            main_menu()
        if option == 3: 
            #If the user selects option 3, run the code that will terminate the program
            main_menu.close()

#Making sure that the program always opens from the main menu
main_menu()


