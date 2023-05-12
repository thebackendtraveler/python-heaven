#!python3

import calculatepay

for i in dir(calculatepay):
    print(i)

import calculatepay

for i in dir(calculatepay.__builtins__):
    print(i)

import calculatepay

for i in dir(calculatepay.__builtins__.__str__):
    print(i)

# Define a string and create placeholders using {}.
my_string = "{} sold {} items."
# Call, the string's format method.
# Pass as many arguments to the format method as there
# are sets of {} in the string.  In this case 2.
print(my_string.format("Olaf",20))

# The same can be done on a string literal,
# without using a pre-defined variable.
print("This example requires {} argument(s).".format(1))

# A numbered index is added inside the {} brackets.
# Note that there are 5 sets of {} but the highest index is 3.
# This means that even though there are 5 items to replace,
# the format method only needs to receive 4 arguments.
# The argument at index 2 will be used twice.
my_string = "{0} sold {1} items. {2} sold {3} items. {2} was the better salesperson."

first_person = "Olaf"
second_person = "Nina"
first_sales = 10
second_sales = 20

# The interpreter looks at the list of arguments and assigns
# them according to their index in the list of arguments as
# the placeholder in the string.
# The indexes for the arguments are as follows:
# 0: first_person
# 1: first_sales
# 2: second_person - will be used twice according to the string
# 3: second_sales
print(my_string.format(first_person, first_sales, second_person, second_sales))

print("f:  {0:f}".format(50.4756))
print(".2f:  {0:.2f}".format(50.4756))
print(".6f:  {0:.6f}".format(50.4756))
print("e:  {0:e}".format(50.4756))
print("b:  {0:b}".format(231))
print("o:  {0:o}".format(231))
print("x:  {0:x}".format(231))
print("X:  {0:X}".format(231))
my_string = my_string = "%s sold %.2f items. %s sold %.2f items."

first_person = "Olaf"
second_person = "Nina"
first_sales = 10
second_sales = 20

print(my_string%(first_person, first_sales, second_person, second_sales))



