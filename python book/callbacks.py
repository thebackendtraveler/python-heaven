#!python3

def subtraction_method(first_value, second_value):
    return first_value - second_value

# Using the method
print(subtraction_method(30,15))

# Doing the same with the lamda expression
subtractor = lambda first_value, second_value: first_value - second_value
print(subtractor(30,15))

def use_function_object(function_object, first_value, second_value):
    return function_object(first_value,second_value)

# Creating the function objects
summing_machine = lambda first_value, second_value: first_value + second_value
subtractor = lambda first_value, second_value: first_value - second_value

# Calling the same function with different results
print(use_function_object(summing_machine, 30, 15))
print(use_function_object(subtractor, 30, 15))

