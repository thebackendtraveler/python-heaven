from myFunction import calculate_area

def main_menu():
    selection = 0
    while selection != 4:
        print("Are you learning Git?: ")
        print("-"*80)
        print("1. Yes, I am")
        print("2. No, i am not learning Git")
        print("3. Lets make a rectangle ")
        print("-"*80)
        print("4. Exit the program")
        print()
        selection = int(input("Please select an option: "))
        print()
        if (selection == 1):
            print("Hello, welcome to the Git course..")
        if (selection == 2):
            print("Hello, you are not a Git student..")
        if (selection == 3):
            print("Making a rectangle and calculating its area...")
            print("-"*80)
            name = input("Enter the name of shape whose area you want to find: ")
            calculate_area(name)
        if (selection == 4):
            print("Exiting the program....")
        else:
            print("-"*80)
            print("OOOPS SOMETHING WENT WRONG. YOU ARE NOT A GIT STUDENT, OR YOU TYPED A WRONG NUMBER. PLEASE TRY AGAIN....")
            print("-"*80)
            print()
            print()

main_menu()