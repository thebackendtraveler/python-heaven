#!python3

value_one = 50
value_two = 70

if value_one > value_two:
    print("Do something")
else:
    # Have to do something, but we don't know what yet.

def placeholder():
    return

value_one = 50
value_two = 70

if value_one > value_two:
    print("Do something")
else:
    print() # calling a print() method - it could also display a message

if value_one > value_two:
    print("Do something")
else:
    placeholder() # calling the placeholder function

print("Statement after ifs")

value_one = 50
value_two = 70

if value_one > value_two:
    print("Do something")
else:
    pass

print("Statement after if")


print("Normal loop:  ", end="")
for value in range(0,5):
    print(value, end="")
print()
print("Looping with continue:  ", end="")
for value in range(0,5):
    if value == 2:
        print("#", end="")
        continue
    print(value, end="")
print()
print("Looping with pass:  ", end="")
for value in range(0,5):
    if value == 2:
        print("#", end="")
        pass
    print(value, end="")
print()
print("Looping with break:  ", end="")
for value in range(0,5):
    if value == 2:
        print("#", end="")
        break
    print(value, end="")




