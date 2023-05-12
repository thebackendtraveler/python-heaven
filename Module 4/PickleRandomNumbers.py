from genericpath import isfile
from random import random
import pickle, os

entries = dict()
file_name = "mypickle.dat"

if os.path.isfile(file_name):
    #The files exists, load the data from the file
    the_saved_pickle_data = open(file_name, "rb")
    entries = pickle.load(the_saved_pickle_data)
    the_saved_pickle_data.close()
else:
    # if the file does not exist, create pickle entries in the entries variable
    for current in range (97, 123):
        entries[chr(current)] = int(random() * 1000)


print(entries)

user_response = input("Do you want to update an entry? (y or n)")

if user_response == 'y':
    the_entry = input("Which key do you want to update? (a to z)")
    the_value = int(input("Enter the value: "))
    entries[the_entry] = the_value

the_new_pickled_data = open(file_name, "wb")
pickle.dump(entries, the_new_pickled_data)
the_new_pickled_data.close()
