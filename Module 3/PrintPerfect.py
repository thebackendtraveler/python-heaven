max_int = int(input("Please enter a maximum value: "))
current = 1

while current <= max_int:
    total = 0

    for i in range(1, current):
        if current % i == 0:
            total += i
        
    if total == current:
            print(current, end =" ")

    current += 1