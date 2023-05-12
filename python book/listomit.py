#!python3

float_list = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1]
print("Initial list:",float_list)

# Slice all values starting with index 3.  Take note of the inclusion of the colon; otherwise, it would simply be a 
normal index of 3 (not a slice).
print("Slice with a start of 3",float_list[3:])

# Slice all values stopping at index 7.  Take note of the inclusion of the colon; otherwise, it would simply be a normal
 index of 7 (not a slice).
print("Slice with a stop of 7",float_list[:7])