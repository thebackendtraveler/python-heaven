#!python3

# a loop that should iterate from 1 to 10

for item in range(1,11):
    print("Item value:",item)
    if input("Enter q to quit or any other key to continue: ") == "q":
        break

total = 0

while total < 10:
    total += 1
    if total % 2 == 0:
        print(total, " is divisible by 2.")
    else:
        continue

