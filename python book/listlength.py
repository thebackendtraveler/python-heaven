#!python3

int_list = [34,656,23,2,45,65,7887,45,2,334,67] # 11 items, lowest index 0, highest index 10
print("Initial list:",int_list)

# To determine the length of a list, i.e. the number of items in the list, use the len() function
print("Length of the list:",len(int_list))

# To add an item to the end of a list, use the list's append() method
int_list.append(77)
print("After append 77:",int_list)

# To add an item at a specific place in the list, use the list's insert() method.  The insert() method
# requires an index at which the value should be inserted and a value to insert.
# The insert doesn't overwrite the value that is already at the specified index; the item at the index simply
# increases its index by 1 to make room for the new item.
int_list.insert(2,55)
print("After insert 55 at index 2:",int_list)

# It is also possible to extend a list by adding the contents of an entire other list to the end of it.
# This is done using the extend() method
another_list = [45,22,11]
int_list.extend(another_list)
print("After extend with 45,22,11:", int_list)

# To remove an item from the list, simply call the method remove() and provide it with the value to remove.
# It will remove the first occurrence of the value.
int_list.remove(2)
print("After remove value 2:",int_list)

# To remove a specific item from a list, use Python's del() function and provide it with an indexed
# item in the list
del(int_list[5])
print("After del index 5:",int_list)

# Another way to remove a list item, using an index, but also return its value is to use the pop()
# method.  Once pop() is provided with an index, it will return the value stored at the index and then
# remove the item from the list.
print("Popped from index 6:",int_list.pop(6))
print("After pop index 6:",int_list)