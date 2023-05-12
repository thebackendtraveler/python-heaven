#!python3

print("1. Print the first menu option")
print("2. Print the second menu option")
print("3. Print the third menu option")
print("4. Print the fourth menu option")
print("")

menuSelection = input("Please select a menu option : ")

if (menuSelection == "1"):

  print("The first option was selected")

else:

    print("Another option was selected ")

print("1. Print the first menu option")
print("2. Print the second menu option")
print("3. Print the third menu option")
print("4. Print the fourth menu option")
print("")

menuSelection = int(input("Please select a menu option : "))


if (menuSelection == 1):

  print("The first option was selected")

elif (menuSelection == 2):

    print("The second option was selected")

elif (menuSelection == 3):

    print("The third option was selected")

elif (menuSelection == 4):

    print("The fourth option was selected")

else:

    print("An invalid selection was used by the end user")

try:
  print("1. Print the first menu option")
    print("2. Print the second menu option")
    print("3. Print the third menu option")
    print("4. Print the fourth menu option")
    print("")
    menuSelection = int(input("Please select a menu option : "))

   if (menuSelection == 1):

                   print("The first option was selected")

elif (menuSelection == 2):

                print("The second option was selected")

        elif (menuSelection == 3):

                print("The third option was selected")

        elif (menuSelection == 4):

                print("The fourth option was selected")

    else:

print("An invalid selection was used by the end user")

except:

    print("Please enter a value between 1 and 4")


