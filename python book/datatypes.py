#!python3

print(type(3))
print(type(7.6))
print(type("Hello"))
print(type(input("Please enter a value:")))

a = "50"

# isinstance is provided with the value to test (i.e. a) and the data type to test against
if isinstance(a,int):
    print("a is an int")
elif isinstance(a,float):
    print("a is a float")
elif isinstance(a,str):
    print("a is an str")

a = 30.675
print("The value of a is", a, "and it is of type", type(a))
print("casting a to int using a = int(a)")
a = int(a)
print("The value of a is", a, "and it is of type", type(a))
print("casting a to float using a = float(a)")
a = float(a)
print("The value of a is", a, "and it is of type", type(a))
print("casting a to str using a = str(a)")
a = str(a)
print("The value of a is", a, "and it is of type", type(a))

