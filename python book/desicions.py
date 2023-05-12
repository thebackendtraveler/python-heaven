#!python3

# if statement to be evaluated:
#    Block of code:  Action to take when the evaluation results in True

a = 5
b = 2

if a * b > 9:  # Note that the if statement ends in :
    print("a * b (", a * b, ") is greater than 9") # Note the indent at the beginning of the line


a = 5
b = 2
print("The if evaluates to true and the second line is indented:")
if a * b > 9:
    print("a * b (", a * b, ") is greater than 9")
    print("This should only print on True")

print()

print("The if evaluates to false and the second line is indented:")
if a * b < 9:
    print("a * b (", a * b, ") is greater than 9")
    print("This should only print on True")

print()

print("The if evaluates to true and the second line is not indented:")
if a * b > 9:
    print("a * b (", a * b, ") is greater than 9")
print("This should only print on True")

print()

print("The if evaluates to false and the second line is not indented")
if a * b < 9:
    print("a * b (", a * b, ") is greater than 9")
print("This should only print on True")

fuel = 10

if fuel > 10:
    print("Keep on driving.")
else:
    print("Stop to refuel.")

fuel = 15

if fuel > 20:
    print("Drive fast.")
elif fuel > 10:
    print("Drive slow.")
else:
    print("Stop to refuel.")

code
fuel = 15

if fuel > 20:
    print("Drive fast.")
else:
    if fuel > 10:
        print("Drive slow.")
    else:
        print("Stop to refuel.")


