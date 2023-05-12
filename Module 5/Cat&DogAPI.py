import thekey
import requests
import json
import webbrowser

#Global URL for the calls
url_dogs = "https://api.api-ninjas.com/v1/dogs"
url_cats = "https://api.api-ninjas.com/v1/cats"

#The function that will do the API calls
def api_call(url, search):
    try:
        querystring = {"name": search}
        headers = {
            'x-api-key': thekey.apikey
        }
        
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        return (json.loads(response.text))[0]
    except: 
        return False

#The function that will display the dog information
def display_dog_information(info):
    print("Family friendly: {}/5".format(info['family_friendly']))
    print("General health: {}/5".format(info['general_health']))
    print("Playfulness: {}/5".format(info['playfulness']))
    print("Children friendly: {}/5".format(info['children_friendly']))
    print("Other pets friendly: {}/5".format(info['other_pets_friendly']))

#The function that will display the cat information
def display_cat_information(info):
    print("Family friendly: {}/5".format(info['family_friendly']))
    print("General health: {}/5".format(info['general_health']))
    print("Playfulness: {}/5".format(info['playfulness']))
    print("Children friendly: {}/5".format(info['children_friendly']))
    print("Other pets friendly: {}/5".format(info['other_pets_friendly']))
   
    
#The main menu function with the option to select
def main_menu():
    selection = 0
    while selection != 3:
        print("-- Main Menu --")
        print("1. Cat Information")
        print("2. Dog Information")
        print("-"*50)
        print("3. Exit")
        print("-"*50)
        print()
        selection = int(input("Please choose a option from the menu: "))
        print()
        #If option one was selected, start the cat sequence
        if (selection == 1):
            breed = input("Which breed do you want to know more about?: ")
            result = api_call(url_cats, breed)
            if (result == False):
                print("There was a problem getting the breed name...")
            else: 
                sub_menu(result, 1)
        
        #If option two was selected, start the dog sequence
        if (selection == 2):
            breed = input("Which breed do you want to know more about?: ")
            result = api_call(url_dogs, breed)
            if (result == False):
                print("There was a problem getting the breed name...")
            else: 
                sub_menu(result, 1)

#The sub menu that comes after selecting dog or cat
def sub_menu(breed_info, type):
    selection = 0
    while selection != 3:
        print("-- Sub Menu --")
        print("1. Display details of the animal and breed")
        print("2. Display image")
        print("-"*50)
        print()
        selection = int(input("Please choose a option from the menu: "))
        print()
        
        if (selection == 1):
            if (type == 1):
                display_cat_information(breed_info)
            else: 
                display_dog_information(breed_info)
        
        if(selection == 2): 
            webbrowser.open(breed_info['image_link'], new=1)

#The code to start the script with the main menu
main_menu()
    
