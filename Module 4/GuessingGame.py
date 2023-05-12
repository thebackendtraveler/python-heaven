import myModules

start_time = myModules.create_time()

guess_another = 'y'

while guess_another == 'y':
    user_value = int(input("Enter a number in the range 1 to 9: "))
    random_number = myModules.generate_random(10)

    if user_value == random_number:
        print("You guessed the correct number!!")
    else: 
        print("Better luck next time, the answer was {0}".format(random_number))
        print("Better luck next time, the answer was ", random_number)

    guess_another = input("Do you want to try again? (y or n)")

end_time = myModules.create_time()

print("You started to play the game at {0}".format(myModules.output_local_time(start_time)))
print("You have played the game for {0} seconds".format(myModules.calculate_difference(start_time, end_time)))