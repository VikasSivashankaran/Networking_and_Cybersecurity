"""
This module contains a function to encrypt a message using the Caesar cipher.
"""

def encrypt(text, shift):
    """
    Encrypts the input text using the Caesar cipher with the given shift.

    Parameters:
    text (str): The string to be encrypted.
    shift (int): The number of positions to shift each character.

    Returns:
    str: The encrypted string.
    """
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

if __name__ == "__main__":
    input_text = input("Enter the string to encrypt: ")
    shift_amount = int(input("Enter a number to shift: "))
    print("Cipher: ", encrypt(input_text, shift_amount))
