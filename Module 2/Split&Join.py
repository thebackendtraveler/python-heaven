#!python3

myStrInput = input('Enter your string to test: ')
mySplInput = input('Enter a character to split on: ')

mySplStr = myStrInput.split(mySplInput)
print(mySplStr)

myCombInput = input('Please enter a character to combine on: ')
myCombString = myCombInput.join(mySplStr)
print(myCombString)

