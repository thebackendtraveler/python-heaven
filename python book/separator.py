#!python3

separator_one = ":"
my_list = [input('What is your name?: '), input('What is your lastname?: '), input('How old are you?: ' ), input('Where do you live?: ' ), input('Are you married?: ')] 

print(";:", separator_one.join(my_list))