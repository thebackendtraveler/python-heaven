#!python3

# Define the function with variable names between the brackets.
# These variable names are referred to as the parameters of
# the function.
# Any arguments passed to the function are received in the
# parameters in the sequence in which they are passed.
# The parameters serve as local variables.

def with_one_argument(first): 
    print("With one argument: first - ", first)
    
def with_two_arguments(first, second):
    print("With two arguments: first - ", first, "second - ", second)

# When calling a function, provide as many arguments as the function
# has parameters.

with_one_argument(10) 
with_two_arguments("one",2)

def display(first, second, third, fourth):
    print("first:", first)
    print("second:", second)
    print("third:",third)
    print("fourth:",fourth)
    
print("Called in sequence:")
display(1,2,3,4)
print()
print("Called by specifying parameter names:")
display(second=2,fourth=4,third=3,first=1)

# The function parameters are provided with default values.
# If no arguments are passed for these parameters, they
# will default to these values.
# This has the effect of making the parameters optional.

def display(first=1, second=2, third=3, fourth=4):
    print("first:", first)
    print("second:", second)
    print("third:",third)
    print("fourth:",fourth)
    
print("Pass all arguments:")
display(1,2,3,4)
print()
print("Pass no arguments:")
display()
print()
print("Pass only the first argument:")
display(88)
print()
print("Pass the first argument and a named argument:")
display(88,fourth=99)

