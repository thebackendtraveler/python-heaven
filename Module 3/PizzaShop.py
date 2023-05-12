Total = 0

print("Please select a pizza base: ")
print("1. Thick")
print("2. Thin")
pizza_base = int(input("Please select a base: "))
base_text = " "

if pizza_base == 1:
    Total += 10
    base_text = "\n"
    base_text = "{0} Kr{1}".format("Thick Base".ljust(20, " "),  "10".rjust(5, " "))
else: 
    Total += 5
    base_text = "\n"
    base_text = "{0} Kr{1}".format("Thin Base".ljust(20, " "),  "5".rjust(5, " "))


print("Please select a pizza size: ")
print("1. Small")
print("2. Medium")
print("3. Large")
pizza_size = int(input("Please select a size: "))
size_text = " "

if pizza_size == 1:
    Total += 30
    size_text = "\n"
    size_text = "{0} Kr{1}".format("Small".ljust(20, " "),  "30".rjust(5, " "))
elif pizza_size == 2:
    Total += 40
    size_text = "\n"
    size_text = "{0} Kr{1}".format("Medium".ljust(20, "2"),  "40".rjust(5, " "))
elif pizza_size == 3:
    Total += 50
    size_text = "\n"
    size_text = "{0} Kr{1}".format("Large".ljust(20, " "),  "50".rjust(5, " "))

print("Please select a pizza sauce: ")
print("1. Tomato")
print("2. Barbeque")
pizza_sauce = int(input("Please select a sauce: "))
sauce_text = " "

if pizza_sauce == 1:
    Total += 5
    sauce_text = "\n"
    sauce_text = "{0} Kr{1}".format("Tomato".ljust(20, " "),  "5".rjust(5, " "))

elif pizza_sauce == 2:
    Total += 10
    sauce_text = "\n"
    sauce_text = "{0} Kr{1}".format("barbeque".ljust(20, " "),  "10".rjust(5, " "))

topping_text = " "

toppings = input("Would you like to add Cheese? (y for yes, and n for no) ")
if toppings == "y":
    Total += 5
    topping_text = "\n"
    toppings_text = "{0} Kr{1}".format("Cheese".ljust(20, " "),  "5".rjust(5, " "))

toppings = input("Would you like to add Mushrooms? (y for yes, and n for no) ")
if toppings == "y":
    Total += 3
    topping_text = "\n"
    toppings_text = "{0} Kr{1}".format("Mushrooms".ljust(20, " "),  "3".rjust(5, " "))

toppings = input("Would you like to add Pineapple? (y for yes, and n for no) ")
if toppings == "y":
    Total += 5
    topping_text = "\n"
    toppings_text = "{0} Kr{1}".format("Pineapple".ljust(20, " "),  "5".rjust(5, " "))

toppings = input("Would you like to add Bacon? (y for yes, and n for no) ")
if toppings == "y":
    Total += 7
    topping_text = "\n"
    toppings_text = "{0} Kr{1}".format("Bacon".ljust(20, " "),  "5".rjust(5, " "))

toppings = input("Would you like to add Chicken? (y for yes, and n for no) ")
if toppings == "y":
    Total += 7
    topping_text = "\n"
    toppings_text = "{0} Kr{1}".format("Chicken".ljust(20, " "),  "3".rjust(5, " "))

toppings = input("Would you like to add Fish? (y for yes, and n for no) ")
if toppings == "y":
    Total += 6
    topping_text = "\n"
    toppings_text = "{0} Kr{1}".format("Fish".ljust(20, " "),  "6".rjust(5, " "))

print()
print(base_text)
print(size_text)
print(sauce_text)
print(topping_text)
print("-"*30)
print("{0} Kr{1}".format("Total".ljust(20, " "), str(Total).rjust(5, " ")))



































