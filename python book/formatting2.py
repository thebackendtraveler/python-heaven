#!python3

the_string = "a king, named George, fell into the gorge."

print("original: ", the_string)

## capitalize() changes the first letter to uppercase
print("capitalize(): ", the_string.capitalize())

## title() changes all first letters of words to uppercase
print("title(): ", the_string.title())

## upper() changes all letters to uppercase
print("upper(): ", the_string.upper())

## lower() changes all letters to lowercase
print("lower(): ", the_string.lower())

## swapcase() changes all uppercase to lowercase and lowercase to uppercase
print("swapcase(): ", the_string.swapcase())

input_string = "this is the string to split"

result_one = input_string.split()
print("Default split (on spaces):")
print(result_one)
print()
result_two = input_string.split("i")
print("Split on i:")
print(result_two)
print()
result_three = input_string.split("is")
print("Split on is:")
# Note that this results in a whitespace element
# since it was surrounded by two 'is' strings
print(result_three)

input_string = "   a string with horizontal whitespace   "

# lstrip() removes leading whitespaces
print("lstrip(): ", input_string.lstrip())

# rstrip() removes trailing whitespaces
print("rstrip(): ", input_string.rstrip())

# strip() removes leading and trailing whitespaces
print("strip(): ", input_string.strip())

