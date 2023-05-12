total = 0
user_value = int(input("Please enter an integer: "))

while user_value != -1:
    total += user_value
    user_value = int(input("Please enter an integer: "))

print("Total value: ", total)