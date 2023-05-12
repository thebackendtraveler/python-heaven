#!python3

first_string = "I am combining "
second_string = "these 2 strings."
new_string = first_string + second_string
print(new_string)

repeat_me = "This string will repeat | "
new_string = repeat_me * 3
print(new_string)

# Just as addition and multiplication may occur in the same equation
# so too may concatenation and repetition be used in the same line.

new_string = "| " + repeat_me * 3
print(new_string)

test_string = "This is my string"
slice_of_test_string = test_string[3]

print("test_string: ", test_string)
print("slice at index 3: ",slice_of_test_string)

test_string = "This is my string"

print("test_string: ", test_string)
print("slice at index 5 up to index 10: ",test_string[5:10])
print("slice at index 5 up to index 10, step 2: ",test_string[5:10:2])
print("slice at index 5 up to the end of the string: ",test_string[5:])
print("slice at index 5 up to 3 characters from the end: ",test_string[5:-3])

test_string = "This is my string" print("Membership inclusive:")print("This" in 
test_string)print("John" in test_string)print()print("Membership exclusive:")print("This" 
not in test_string)print("John" not in test_string)

print("This is a \t string") # Normal behaviour
print(r"This is a \t string") # Interpreted as a raw string

def my_test_function():
    '''This is a function to demonstrate the use of a docstring'''
    return

print(my_test_function.__doc__)

print(input.__doc__)

