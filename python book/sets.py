#!python3

colour_set = {"black", "blue", "green", "orange", "white"}
print("Initial set:", colour_set)

# Use the add() method to add values to the set
colour_set.add("purple")
print("After add() of purple:",colour_set)

# Use the discoard() method to remove values from the set
colour_set.discard("green")
print("After discard() of green:",colour_set)

# Use the intersection() method to determine which values appear in 2 sets
other_set = {"orange","blue","red","brown"}
print("Other set:",other_set)
print("Intersection of colour and other set:", colour_set.intersection(other_set))

# Use the difference() method to determine which values appear in the first set, but not in the second
print("Difference of colour and other set:", colour_set.difference(other_set))