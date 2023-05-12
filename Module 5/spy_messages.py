#  Import the module that we will use fernet
from cryptography.fernet import Fernet


theKey = b'DaVDce6E7CAIvH16-BYzSfhbWqOd_RIJmKQ3ZR6YR1M='


# Decrypting function
def decrypt_message(enc_message, key):
    #  We check to see if the key has been set if not we will inform the user and return to the main menu
    if key == "b'DaVDce6E7CAIvH16-BYzSfhbWqOd_RIJmKQ3ZR6YR1M='":
        print("Please set the key first\n\n")
        return

    # We set the key
    fernet = Fernet(theKey)
    # We convert the message to bytes, the message will be pasted as string not bytes
    enc_message = bytes(enc_message, "utf-8")
    print("The decrypted message is: ")
    print("*" * 50)
    # We decrypt the message
    dec_message = fernet.decrypt(enc_message).decode()
    # We display the message to the user.
    print(dec_message)
    print("*" * 50 + "\n\n")

# With this function we will encrypt a normal string mesage


def encrypt_message(message, key):
    global theKey
    #  We check to see if the key has been set if not we will inform the user and return to the main menu
    if key == "b'DaVDce6E7CAIvH16-BYzSfhbWqOd_RIJmKQ3ZR6YR1M='":
        print("Please set the key first\n\n")
        return
    # We set the key
    fernet = Fernet(theKey)
    print("The encrypted message is: ")
    print("*" * 50)
    # We encrypt the string value
    enc_message = fernet.encrypt(message.encode())
    # We print the encrypted bytes to the user
    print(enc_message)
    print("*" * 50 + "\n\n")


def main_menu():
    global theKey
    choice = 0
    # We loop the main menu until the users exits the system.
    while choice != 4:
        print("1. Decrypt message ")
        print("2. Encrypt Message")
        print("3. Set the key ")
        print("*"*50)
        print("4. Exit")
        choice = int(input("Please select an option: "))

        if choice == 1:
            encrypted_message = input(
                "Please provide the encrypted message to be decrypted: ")
            decrypt_message(encrypted_message, theKey)

        if choice == 2:
            message = input("Please provide the  message to encrypt: ")
            encrypt_message(message, theKey)

        if choice == 3:
            theKey = input('Please enter the key value: ')
            theKey = bytes(theKey, "utf-8")


main_menu()
