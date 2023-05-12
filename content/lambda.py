
#Add 20 to argument a, and print the result
x = lambda a : a + 20
print("The x is: ", x(10))

#Multiply argument a with argument b and print the result
x = lambda a, b : a * b
print("The x is: ", x(25,6))

#Summarize argument a, b and c and print the results
x = lambda a, b, c : a + b+ c
print("The x is: ", x(10, 20, 30))

#Making a function that will return double of any number entered
def myFunction(n):
    return lambda a : a * n

myDouble = myFunction(2)
print("N is: ", myDouble(12))


#making a function that will return triple of any number entered
def myFunction(n):
    return lambda a : a * n

myTriple = myFunction(3)
print("N is: ", myDouble(12))

#Making a function that will return double / triple
#of any number entered
def myFunction(n):
    return lambda a : a * n

myDouble = myFunction(2)
myTriple = myFunction(3)
print("N is: ", myDouble(12))
print("N is: ", myTriple(12))

#Putting a lamba function inside a function
def myFunction(n):
    x = lambda a : a + n 
    print("The N is: ", x(5, 10))