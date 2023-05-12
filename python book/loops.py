#!python3

total = 0

print("if statement output:\n")

if total < 5:
    print("Total:",total)
    total += 1

total = 0

print("\nwhile statement output:\n")

while total < 5:
    print("Total:",total)
    total += 1

user_choice = input("Enter q to exit or another key to continue: ")

while user_choice != "q":
    print("The user entered:",user_choice)
    user_choice = input("Enter q to exit or another key to continue: ")

print("\nThe user quit the loop.")

outside_counter = 0

while outside_counter < 3:
    inside_counter = 0
    while inside_counter < 3:
        print("Outside counter:",outside_counter,"Inside
              counter:",inside_counter)
        inside_counter+=1
    outside_counter+=1


months = ("January", "February", "March")
number_of_sales = [45,59,34]
class_sizes = {"PRG":30,"NET":40,"NIX":37}

# Simple iteration over strings
for item in months:
    print(item, end=" ")

print()

# Simple iteration over integers
for item in number_of_sales:
    print(item, end=" ")

print()

# Simple iteration over a string.  Since a string is just a list of characters, it may be iterated over.
for item in "The string":
    print(item, end=" ")

print()

 # enumerate() allows the elements in a data structure to be listed along with its index in the data structure
for item in enumerate(months):
    print(item, end=" ")

print()

 # zip() allows the elements in multiple data structures to be iterated at the same time
for item in zip(months , number_of_sales):
    print(item, end=" ")

print()

 # Use key, value combinations to iterate through a dictionary's items()
for key, value in class_sizes.items():
    print(key, ": ", value,sep="")


# When a range() is provided with a single value, the single value constitutes the length, i.e.
# the range is from 0 to 1 less than the value specified
print("range(10)",end=":  ")
for item in range(10):
    print(item,end=",")

# When a range() is provided with 2 values, the first value constitutes the minimum value and the
# second the maximum, the range is from the minimum value to 1 less than the maximum value specified
print("\nrange(1, 10)",end=":  ")
for item in range(1, 10):
    print(item,end=",")

# When a range() is provided with 3 values, the third value constitutes the step size. A step size of 2
# would iterate through every second value, 3 every third and so forth.
print("\nrange(1, 10, 2)",end=":  ")
for item in range(1, 10, 2):
    print(item,end=",")



