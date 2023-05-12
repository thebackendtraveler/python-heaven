sales_values = list()

while input("Do you want to enter a sales value? (y or n)") == 'y':
    try:
        value = float(input("Please enter a sales value: "))
        sales_values.append(value)
    except ValueError:
        print("Please ensure that you have a correct sales value...")

print("You have entered ", len(sales_values), "sales values")

while True:
    number_of_sales = -1
    try: 
        number_of_sales = int(input("Number of sales: "))
        total = 0
        try:
            for i in range(0, number_of_sales):
                total += sales_values[i]
        except IndexError:
            print("Please ensure that the number of sales is in the range of o to ", len(sales_values))

        print("Sales total: ", total)
        break
    except ValueError:
        print("Please ensure that you have the correct number of sales...")
        continue