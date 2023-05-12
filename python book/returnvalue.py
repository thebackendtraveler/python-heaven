#!python3

a = input("Enter a value:  ")
print(a)
print(input("Enter another value:  "))

def add_values(first_value, second_value):
    return first_value + second_value

# Assigning the returned value to a variable
result = add_values(10, 5) 
print(result)
# Using the returned value in-line without declaring a variable
print(add_values(20,10))

def calculator(calc_type, first_value, second_value):
    if calc_type == 1:
        print("Adding values")
        return first_value + second_value
    elif calc_type == 2:
        print("Subtracting values")
        return first_value - second_value
    elif calc_type == 3:
        print("Undefined")
        return
    
print(calculator(1,20,10))
print(calculator(2,20,10))
print(calculator(3,20,10)) # The return statement returns nothing
print(calculator(4,20,10)) # No return statement matches this calc_type

def calc_all(first_value, second_value):
    Addition = first_value + second_value
    Subtraction = first_value - second_value
    Division = first_value / second_value
    Multiplication = first_value * second_value
    return Addition, Subtraction, Division, Multiplication # all 4 values are 
returned

# Receiving the values separately
first, second, third, fourth = calc_all(20,10)
print(first, second, third, fourth)
#receiving all the values at once
values = calc_all(30,15)
print(values)

def calc_all_separate_returns(first_value, second_value):
    Addition = first_value + second_value
    Subtraction = first_value - second_value
    Division = first_value / second_value
    Multiplication = first_value * second_value
    return Addition
    return Subtraction
    return Division
    return Multiplication

values = calc_all_separate_returns(20,10)
print(values)

