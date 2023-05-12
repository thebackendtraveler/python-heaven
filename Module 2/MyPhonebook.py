#!python3

#Define a dictionary consising of business namesphonenumbers
dict_phonebook = {
        'Normal': 40978564, 
        'CoopObs': 41297834, 
        'Meny': 45678923, 
        'Rusta': 48976541, 
        'Power': 49867245
        }

#Request the user of another business name and phone number
phonebook_company = (input('Name a business name: '))
phonebook_number = (input('What is their phone number?: '))
dict_phonebook[phonebook_company] = phonebook_number

#Ask the user to list a business name that already exists, and display the results to the user
phonebook_search = input('Enter another company name that already exists, to show their name and phone number: ')
print(dict_phonebook[phonebook_search])

#Display only business names
print('Display only the business names: ',dict_phonebook.keys())

print('Full dictionary', dict_phonebook)