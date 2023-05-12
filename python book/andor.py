#!python3

username = input("Please enter your username")
password = input("Please enter your password")
userRole = input("Please enter your role id")

if (username == "student") and (password == "noroff"):

  if (userRole <= "1") and (userRole >= "5"):

        print("You have been logged in")

    else:

        print("You cannot login to the system due to your user role")

else:

    print("Username and password combination is not valid")

