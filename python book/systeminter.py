#!python3

import sys

print("Python version: ", sys.version)
print("Python interpretor: ", sys.executable) # File path of the Python interpreter

print("Folders where Python searches for modules:")
for folder in sys.path:
    print(folder)

import sys

help()

import keyword

print("Python keywords:")
for theword in keyword.kwlist:  # kwlist contains a list of Python 
keywords
    print(theword, end=", ")
print()
# iskeyword returns True or False depending on whether a word is a keyword
print("Noroff is a Python keyword: ", keyword.iskeyword("Noroff"))


