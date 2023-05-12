i = 1
while i < 10:
    print("The current iteration is: ", i)
    i += 1 
else: 
    print("The iteration has stopped..")
    
   
    
option = 0
while option != 1:
    option = int(input("What is your favorite number?: "))
    print("Your favorite number is".ljust(30), option)
else: 
    print("The number you entered is not correct")
    
  