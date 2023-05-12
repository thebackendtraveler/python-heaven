
print("-" * 30)
print("Menu System")
print("-" * 30)
print("1. Guess the number")
print("2. Print something")
print("3. Change a print option")
print("-" * 30)
option = int(input("Please select an option: "))

message = ["Welcome, you passed the certification"]

if option == 1:
    guess_number = int(input("Please enter a number: "))
    if guess_number == 543:
        print("You guessed the right number!! It was 543.")
    elif guess_number < 543:
        print("The number is too low. Try again...")
    elif guess_number > 543:
        print("The number is too high. Try again...")

if option == 2:
    strIndex = int(input("Please enter a number between 0 and 3: "))
    if strIndex >= 0 and strIndex <= 3:
        print(message[strIndex])
    else:
        print("Please enter a valid number between 0 and 3. Try again...")

if option == 3:
    strIndex = int(input("Which index do you want to change? Between 0 and 3"))
    strChange = input("What do you want to replace it with?")

    if strIndex >= 0 and strIndex <= 3:
        message[strIndex] = strChange
        print(message)
    else: 
        print("Please enter a valid number 0 and 3, then try again...")
  