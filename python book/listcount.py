#!python3

int_list = [34,656,23,2,45,65,7887,45,2,334,67]
print("Initial list:",int_list)

# To find the first occurrence of a value in the list, use the index() method and provide it with the value
# to search for
print("The first index of value 2:",int_list.index(2))

# To find the number of times a value appears in the list, use the count() method and provide it with the
# value to count
print("The number of times 2 appears in the list:", int_list.count(2))