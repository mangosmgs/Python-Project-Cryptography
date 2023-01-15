from crypto_functions import *

def print_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print("==========================")
    for key, value in menu.items():
        print(f"{key} = {value}")
    print("==========================")

the_menu = {
    "E" : "Encrypt a message",
    "D" : "Decrypt a message",
    "S" : "Save encryption to file",
    "R" : "Retrieve decryption from file",
    "Q" : "Quit this program"}

cipher_menu = {
    "T": "Scytale Cipher",
    "V": "Vigenere Cipher"
}

opt = None

while True:
    print_menu(the_menu)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper()

    if opt not in the_menu:
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q':
        print("Goodbye!")
        break
  
    if opt == 'E':
        print("::: Which cipher to use?")
        print_menu(cipher_menu)
        cipher = input("> ").upper()
        if cipher == 'T':
            message = input("::: Message > ")
            nColumns = input("::: Key > ")

            if not nColumns.isnumeric():
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue
            else:
                nColumns = int(nColumns)
            
            result = encrypt_transposition(message, nColumns)
        elif cipher == 'V':
            message = input("::: Message > ")
            secret = input("::: Secret > ")
            result = encrypt_vigenere(message, secret)
        else:
            print(f"WARNING: {cipher} is an invalid cipher.\n")
            continue
        
        print(f"Encryption using the {cipher_menu[cipher]}:")
        print(result)

    if opt == 'D':
        print("::: Which cipher to use?")
        print_menu(cipher_menu)
        cipher = input("> ").upper()
        if cipher == 'T':
            message = input("::: Ciphertext > ")
            nColumns = input("::: Key > ")

            if not nColumns.isnumeric():
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue
            else:
                nColumns = int(nColumns)
            
            result = decrypt_transposition(message, nColumns)
        elif cipher == 'V':
            message = input("::: Ciphertext > ")
            secret = input("::: Secret > ")
            result = decrypt_vigenere(message, secret)
        else:
            print(f"WARNING: {cipher} is an invalid cipher.\n")
            continue
        
        print(f"Decrypted message using the {cipher_menu[cipher]}:")
        print(result)

    if opt == 'S':
        print("::: Proceed to save the message that was previously encoded?")
        proceed = input("Press 'y' to continue.\n> ")
        if proceed != 'y':
            continue
        else:
            filename = input("Enter the name of the file.\n> ")
            ...
            print(f"Saved '{filename}'")
        
    if opt == 'R':
        filename = input("Enter the name of the file to open.\n> ")
        if filename:
            print(f"Contents of '{filename}':")
            ...
        else:
            print(f"File '{filename}' was not found.")
 
    input("::: Press Enter to return to main menu")

print("Your secrets are safe with me.")
