from cryptography.fernet import Fernet


theKey = b'DaVDce6E7CAIvH16-BYzSfhbWqOd_RIJmKQ3ZR6YR1M='

#The decrypting function
def decrypt_message(encrypted_msg, key):
    global theKey
    if key == "":
        print("Please set the key first\n\n")
        return

    fernet = Fernet(key)
    encrypted_msg = bytes(encrypted_msg, "utf-8")
    print("The decrypted message is: ")
    print("*" * 50)
    decrypted_msg = fernet.decrypt(encrypted_msg).decode()
    print(decrypted_msg)
    print("*" * 50 + "\n\n")
    
#The encrypting function
def encrypt_message(message, key):
    global theKey
    if key == "":
        print("Please set the key first\n\n")
        return
    fernet = Fernet(theKey)
    print("The encrypted message is: ")
    print("*" * 50 + "\n\n")
    encrypted_msg = fernet.encrypt(message.encode())
    print(encrypted_msg)
    print("*" * 50 + "\n\n")
    
#The main menu
def main_menu():
    global theKey
    choice = 0
    while choice != 4:
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Define a key")
        print("*"*50)
        print("4. Exit")
        choice = int(input("Please select an option: "))
        
        if choice == 1:
            message = input("Please provide a message to encrypt: ")
            encrypt_message(message, theKey)
        
        if choice == 2:
            encrypted_message = input("Please provide the encrypted message you want to decrypt: ")
            decrypt_message(encrypted_message, theKey)
            
        if choice == 3:
            theKey = input("Please enter the new key value: ")
            theKey = bytes(theKey, "utf-8")

main_menu()