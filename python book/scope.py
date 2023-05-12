#!python3

print(a)
a = 70

a = 70
print(a)

price = 70

name = input("Please enter your name:  ")
amount = int(input("How many items do you wish to purchase?  "))
total = amount * price
print(name,", your total for ",amount," items is: ",total, sep="")

name = input("Please enter your name:  ")
amount = int(input("How many items do you wish to purchase?  "))
total = amount * price
print(name,", your total for ",amount," items is: ",total, sep="")

name = input("Please enter your name:  ")
amount = int(input("How many items do you wish to purchase?  "))
total = amount * price
print(name,", your total for ",amount," items is: ",total, sep="")

def calculate_person_total():  # Function header, the rest is the function body
    name = input("Please enter your name:  ")
    amount = int(input("How many items do you wish to purchase?  "))
    total = amount * price
    print(name,", your total for ",amount," items is: ",total, sep="")
    # Take note the indent.  If the statements were not indented, they would not
    # form part of the function.  Similarly to what we saw with the if statement.

def calculate_person_total(): 
    name = input("Please enter your name:  ")
    amount = int(input("How many items do you wish to purchase?  "))
    total = amount * price
    print(name,", your total for ",amount," items is: ",total, sep="")

price = 70

while (input("Type 'y' to calculate a user's details:  ") == 'y'):
    calculate_person_total()

# Functions

def calculate_person_total(): 
    name = input("Please enter your name:  ")
    amount = int(input("How many items do you wish to purchase?  "))
    total = amount * price
    print(name,", your total for ",amount," items is: ",total, sep="")

# Main script
    
price = 70

while (input("Type 'y' to calculate a user's details:  ") == 'y'):
    calculate_person_total()
    
print(total) # total only exists in the function

# Functions

def calculate_person_total(): 
    
    def inner_function():  # This function is declared within the scope of the other
 function
        print("inner function called")
        inner_variable = 50
        
    name = input("Please enter your name:  ")
    amount = int(input("How many items do you wish to purchase?  "))
    total = amount * price
    print(name,", your total for ",amount," items is: ",total, sep="")
    inner_function()

# Main script
    
price = 70

while (input("Type 'y' to calculate a user's details:  ") == 'y'):
    calculate_person_total()

inner_function() # inner_function() only exists inside calculate_person_total()

def calculate_person_total(): 
    
    def inner_function():  
        global inner_variable # Variable declared global
        print("inner function called")
        inner_variable = 50
    
    global total # Variable declared global
    name = input("Please enter your name:  ")
    amount = int(input("How many items do you wish to purchase?  "))
    total = amount * price 
    print(name,", your total for ",amount," items is: ",total, sep="")
    inner_function()



# Main script
    
price = 70

while (input("Type 'y' to calculate a user's details:  ") == 'y'):
    calculate_person_total()
    
print("Price:",price) # local variable
print("Total:",total) # global variable
print("Inner variable:", inner_variable) # global variable

