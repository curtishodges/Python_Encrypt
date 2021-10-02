# Basic encryption program
# Takes a user input
# Reverses the users input then converts each character into ascii
# Multiples the ascii values by a randomly chosen key
from random import *


def welcome():
    print("Please ensure that you keep the generated key safe as this is the only way to decrypt messages")


def encrypt():
    key = randint(1000, 10000)  # Randomly generates a encryption key for the user
    print("Your generated encryption key is : " + str(key))
    plain_text = input("Please enter the message you would like to encrypt: ")
    reverse_plain_text = plain_text[::-1] # Reverses the users message so it is backwards e.g Hello would turn to olleH
    ascii_value = []
    for i in reverse_plain_text: # Converts each character in the users message into it's ascii value
        ascii_value.append(ord(i))
    ascii_multiplied = [x * key for x in ascii_value] # Multiplies the ascii values by the randomly generated key
    separator = " "
    print("Encrypting message...")
    print("___________________________________________________")
    print("Your message has been encrypted : \n" + separator.join(map(str, ascii_multiplied))) # prints the users
    print("___________________________________________________")
    # encrypted message


def decrypt():
    key = int(input("Please enter your decryption key: "))
    encrypted_message = input("Please enter your encrypted message: ")
    reverse_encrypted_message = encrypted_message[::1]
    decrypt_message = [int(i) for i in reverse_encrypted_message.split()]
    decrypt_message_undone = [i // key for i in decrypt_message]
    decrypted_message = "".join(chr(i) for i in decrypt_message_undone)
    print("Decrypting message...")
    print("___________________________________________________")
    print("Your decrypted message is: \n" + str(decrypted_message)[::-1])
    print("___________________________________________________")


def main_menu_encryption():
    print("Please select from the following: ")
    main_menu_choice = int(input("1: Encrypt a message 2: Decrypt a message "))
    if main_menu_choice == 1:
        encrypt()
    if main_menu_choice == 2:
        decrypt()
    else:
        return main_menu_encryption()
