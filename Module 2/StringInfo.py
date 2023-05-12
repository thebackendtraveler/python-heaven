#!python3

myInputStr = input('Please enter a string of text: ')
print('The length of the string is ', len(myInputStr))

myWord = input('Please enter a word in the string: ')
myWordIndex = myInputStr.index(myWord)
print('The index of the word in the string is: ', myWordIndex)

firstSection = myInputStr[0:myWordIndex]
secondSection = myInputStr[myWordIndex + len(myWord):]

print(firstSection + '\'' + myWord + '\'' + secondSection)