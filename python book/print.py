import os





option = "Say Hello"
choice = "Exit"

#main menu


def main_menu():
    choice = 0
    while choice != 3:
        print("-"*80)
        print("1. Say Hello")
        print("2. Ask what you want to do now?")
        print("3. Exit")
        print("-"*80)
        choice = int(input("Please choose an option: "))
        
        if choice == 1: 
            print(f'Hello, {os.getlogin()}! How is it going?')
            
        if choice == 2:
            print(f'Hello,  {os.getlogin()}! What do you want to do now?')
            
            
main_menu()