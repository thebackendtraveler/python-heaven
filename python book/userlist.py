#!python3

int_list1 = [' ']
int_list2 = [' ']

int_list1 = [ input('What is yout name?: '), input('What is your age?: ')]
int_list2 = [ input('What is your favourite car?: '), input('Do you have a job?: '), input('Do you have a house?: ')]

multi_list = [int_list1, int_list2]

print(multi_list)
del(int_list2[2])
print('After del index 2: ', multi_list)


multi_list = [int_list1, input('Where do you live?: '), int_list2]

print('Slice with start 2 and stop 4: ',multi_list)