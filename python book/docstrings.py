help(dir)
print(dir.__doc__)

class MyClass:
    something = 0
    # Sets the docstrings property of the class
    __doc__ = "This is an overview of what MyClass does."

    def my_class_function():
        # A one-line docstring for this method
        '''This is an overview of what my_class_function does'''
        print("Called MyClass function")


def my_function():
    print("Called function")

# Sets the docstrings property of the function.
my_function.__doc__ = "This is an overview of what MyFunction does."

help(MyClass)
print()
help(my_function)

def my_other_method():
    """This is a
    mult-line
    descriptive
    docstring."""
print("Called my_other_method.")

help(my_other_method)

"""The first line serves as a summary

This is a description of the functionality. Any information
important to the usage of the object should be added here.
"""

# A blank line should be left between the docstring and any code

import argparse

# Creates an ArgumentParser object which will hold all the necessary information
# to parse the values from the command line.
parser = argparse.ArgumentParser(description='Used to process integers.')

# The add_argument method is used to provide arguments which may be used on
# the command line:
# - The first argument defines the name or flags, in the format -flag or --flag
# - The metavar argument provides a shorthand name for the argument in usage messages
# - The type argument specifies to which type the argument should be converted
# - The nargs argument specifies the number of command line arguments that may be provided,
# it may be a number, a ? specifies that the argument is optional or otherwise a single argument,
# * specifies that all arguments will be gathered into a list, + also specifies that all arguments
# will be gathered into a list (if not at least one argument is passed an error will be generated).
# A value of argparse.REMAINDER specifies that all remaining arguments will be parsed into a list.
# - The help argument provides a short description of what the argument does.
parser.add_argument('integers', metavar='N', type=int, nargs='+',
help='an integer to add')
# - The dest argument specifies the name of an attribute to be associated with the argument
# and added to the object returned by calling parse_args() on the ArgumentParser object.
# - The action argument specifies the basic type of action that this argument will take
# when encountered. In this case, store_const would store the value specified by the const
# argument.
# - The const argument specifies a constant value required by some action and nargs selections.
# This argument specifies that when the argument is provided the result of calling the sum()
# method on the list should be stored.
# - The value produced whenever this argument is omitted from the command line. In this case,
# the default argument specifies that if the argument is not used on the command line that
# the list's max() method be called and the value stored.
parser.add_argument('--total', dest='calc', action='store_const',
const=sum, default=max,
help='totals the integers or finds the maximum (default)')

# Inspects the command line, parses any received arguments and executes the specified actions.
# In this case it will return 2 arguments, one called integers which will return a list of 1
# or more integers and calc attribute which will either be an alias for the sum or the max
# list method.
args = parser.parse_args()
# Displays the result of the accumulate method (either sum() or max()), being applied to the
# list of integers received
print(args.calc(args.integers))