#!python3

value_a = 10

try:
    print(value_b) # value_b has not been initialized and will result in a runtime error
except:
    print("An error has occurred")

value_a = 10

try:
    print(value_b) # value_b has not been initialized and will result in a run-time error
except NameError as msg:  # The NameError exception is handled, and its details
                          # are stored in msg using the as keyword
    print("An error has occurred: ",msg )

the_list = [1,2,3,4] # A list with 4 elements

try:
    for i in range (0,5):  # A loop with 5 iterations
        print(the_list[i],end=",")
except IndexError as msg:
    print()
    print("An error has occurred: ", msg)

try:
    a = int(input("Enter a number:  "))
except ValueError as msg:
    print("An error has occurred: ", msg)

entries = [2,3,4,5,6]
try:
    a = int(input("Enter a number:  "))
    index = 0
    while index < a:
        print(entries[index])
        index+=1
except (ValueError,IndexError) as msg:
    print("An error has occurred: ", msg)

entries = [2,3,4,5,6]
try:
    a = int(input("Enter a number:  "))
    index = 0
    while index < a:
        print(entries[index])
        index+=1
except (ValueError,IndexError) as msg:
    print("An error has occurred: ", msg)
finally:
    print("This code always executes.")

try:
    a = 50
    if a > 10:
      # Creates a ValueError object with a custom message
      # The raise keyword passes the Error to the except block
      raise ValueError("The value is too high")
except ValueError as msg:
    print("An error has occurred: ", msg)


entries = [2,3,4,5,6]
try:
    a = int(input("Enter a number:  "))
    index = 0
    while index < a:
        print(entries[index])
        index+=1
except Exception as msg:
    print("An error has occurred: ", msg)
finally:
    print("This code always executes.")




