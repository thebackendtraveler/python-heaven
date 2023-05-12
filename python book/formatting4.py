#!python3

input_string = "one two three four one two three four one two three four"
print("Input string: ", input_string)

# count may be used to count the number of occurrences of a substring
print("Count of one: ", input_string.count("one"))
print("Count of five: ", input_string.count("five"))

# find is used to find the index of the first occurrence of the sub-string
print("Index of one: ", input_string.find("one"))
print("Index of two: ", input_string.find("two"))
print("Index of three: ", input_string.find("three"))
print("Index of four: ", input_string.find("four"))
# find returns an index of -1 if the substring could not be found
print("Index of five: ", input_string.find("five"))

# startswith is used to determine if a substring is located
# at the start of a string
print("starts with one? ", input_string.startswith("one"))
print("starts with two? ", input_string.startswith("two"))
print("starts with three? ", input_string.startswith("thre"))
print("starts with four? ", input_string.startswith("four"))
print("starts with five? ", input_string.startswith("five"))

# endswith is used to determine if a substring is located
# at the start of a string
print("ends with one? ", input_string.endswith("one"))
print("edns with two? ", input_string.endswith("two"))
print("ends with three? ", input_string.endswith("thre"))
print("ends with four? ", input_string.endswith("four"))
print("ends with five? ", input_string.endswith("five"))

# isalpha returns true if all characters in the string are letters
print("isalpha - aaaaa:", "aaaaa".isalpha())
print("isalpha - 11111:", "11111".isalpha())
print("isalpha - 11a11:", "11a11".isalpha())
print("-" * 30)
# isnumeric returns true if all characters in the string are numbers
# this includes numbereric characters for any language
print("isnumeric - aaaaa:", "aaaaa".isnumeric())
print("isnumeric - 11111:", "11111".isnumeric())
print("isnumeric - 11a11:", "11a11".isnumeric())
print("-" * 30)
# isdigit returns true if all characters in the string are in
# the range 0 to 9.
print("isdigit - aaaaa:", "aaaaa".isdigit())
print("isdigit - 11111:", "11111".isdigit())
print("isdigit - 11a11:", "11a11".isdigit())
print("-" * 30)
# isalnum returns true if all characters are either numbers or letters
print("isalnum - aaaaa:", "aaaaa".isalnum())
print("isalnum - 11111:", "11111".isalnum())
print("isalnum - 11a11:", "11a11".isalnum())
print("-" * 30)
# islower tests if all characters are lowercase
print("islower - aaaaa:", "aaaaa".islower())
print("islower - BBBBB:", "BBBBB".islower())
print("-" * 30)
# isupper tests if all characters are uppercase
print("isupper - aaaaa:", "aaaaa".isupper())
print("isupper - BBBBB:", "BBBBB".isupper())
print("-" * 30)
# istitle tests if the string is in title case
print("istitle - is this title case?:", "is this title case?".istitle())
print("istitle - Is This Title Case?:", "Is This Title Case?".istitle())
print("-" * 30)
# isspace tests if the string contains only whitespace characters
print("isspace - a:", "a".isspace())
print("isspace -   :", "  ".isspace())
print(r"isspace - \t\t:", "\t\t".isspace())




