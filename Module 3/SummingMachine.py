def summing_machine():
    total = 0
    user_value = input("Please input a number: ")

    while user_value != 's':
        total += int(user_value)
        user_value = input("Please enter a number: ")
    
    return total

if __name__ == "__main__":
    print(summing_machine())