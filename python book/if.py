#!python3

username = input("Please enter your username")
password = input("Please enter your password")
if (username == "student"):
      if (password == "noroff"):
                print("You have been logged in")
        else:
                print("The password is not correct")
else:
        print("The username is not correct")


username = input("Please enter your username ")
password = input("Please enter your password ")

if (username == "student") and (password == "noroff"):

  print("You have been logged in")

else:

    print("Username and password combination is not valid")


department = input("Please enter your department")

if (department == "IT") or (department == "Networking"):

  print("You have access to the networking and IT data")

else:

    print("Welcome, you do not have access to the networking and IT data")


