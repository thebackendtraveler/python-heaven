#!python3

separator_one = ";"
separator_two = ","
separator_three = "###"

the_list = ["1","2","3","4"]

# Call join on the preferred separator and pass the list
# whose elements need to be joined as an argument.

print(";:",separator_one.join(the_list))
print(",:",separator_two.join(the_list))
print("###:",separator_three.join(the_list))