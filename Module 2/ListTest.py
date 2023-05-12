#!python3

#Define a list
input_list = []

#Request 10 names
input_list.append(input('Name friend one: ')) 
input_list.append(input('Name friend two: ')) 
input_list.append(input('Name friend three: ')) 
input_list.append(input('Name friend four: ')) 
input_list.append(input('Name friend five: ')) 
input_list.append(input('Name friend six: ')) 
input_list.append(input('Name friend seven: ')) 
input_list.append(input('Name friend eight: ')) 
input_list.append(input('Name friend nine: ')) 
input_list.append(input('Name friend ten: ')) 

#Sorting the list
input_list.sort()
print('Sorted list:', input_list)

#Reversing the list
input_list.reverse()
print('Reversed list:', input_list)

#Ask the user for another name and append the name to the original list
input_list.append(input('Name one more friend: '))

#Display the contents of the original list
print(input_list)

