#!python3

myStrInput = input('Enter your string to start: ')
mySplInput = input('enter a character to split on: ')

mySplStr = myStrInput.split(mySplInput)
print(mySplStr)

myCombInput = input('please enter a character to combine on: ')
myCombString = myCombInput.join(mySplStr)
print(myCombString)

print('hello')