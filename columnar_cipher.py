def encrypt_columnar_transposition(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    
    # Create the matrix to store the text
    matrix = ['' for _ in range(key)]
    
    # Fill the matrix with characters in columnar fashion
    for i, char in enumerate(plaintext):
        matrix[i % key] += char
    ciphertext = ''.join(matrix)
    
    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    # Calculate the number of rows
    num_rows = len(ciphertext) // key
    
    # Create the matrix to store the text
    matrix = ['' for _ in range(key)]
    
    # Fill the matrix with characters in row-wise fashion
    index = 0
    for i in range(key):
        matrix[i] = ciphertext[index:index + num_rows]
        index += num_rows
    
    # Read the plaintext row by row
    plaintext = ''
    for i in range(num_rows):
        for j in range(key):
            if i < len(matrix[j]):
                plaintext += matrix[j][i]
    
    return plaintext

# Get input from the user
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (number of columns): "))

ciphertext = encrypt_columnar_transposition(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted_text = decrypt_columnar_transposition(ciphertext, key)
print(f"Decrypted: {decrypted_text}")