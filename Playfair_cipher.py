def generate_key_matrix(key):
    key = "".join(sorted(set(key), key=key.index)).replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []
    used_chars = set(key)
    
    for char in key:
        key_matrix.append(char)
        
    for char in alphabet:
        if char not in used_chars:
            key_matrix.append(char)
            
    return [key_matrix[i * 5:(i + 1) * 5] for i in range(5)]

def format_plaintext(plaintext):
    plaintext = plaintext.upper().replace("J", "I")
    formatted_text = ""
    i = 0
    
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else "X"
        
        if a == b:
            formatted_text += a + "X"
            i += 1
        else:
            formatted_text += a + b
            i += 2
            
    if len(formatted_text) % 2 != 0:
        formatted_text += "X"
        
    return formatted_text

def find_position(char, key_matrix):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None, None

def playfair_encrypt(plaintext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = format_plaintext(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row_a, col_a = find_position(a, key_matrix)
        row_b, col_b = find_position(b, key_matrix)
        
        if row_a == row_b:
            ciphertext += key_matrix[row_a][(col_a + 1) % 5] + key_matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += key_matrix[(row_a + 1) % 5][col_a] + key_matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += key_matrix[row_a][col_b] + key_matrix[row_b][col_a]
            
    return ciphertext

def playfair_decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(a, key_matrix)
        row_b, col_b = find_position(b, key_matrix)
        
        if row_a == row_b:
            plaintext += key_matrix[row_a][(col_a - 1) % 5] + key_matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += key_matrix[(row_a - 1) % 5][col_a] + key_matrix[(row_b - 1) % 5][col_b]
        else:
            plaintext += key_matrix[row_a][col_b] + key_matrix[row_b][col_a]
            
    return plaintext

def main():
    key = input("Enter the encryption key: ").upper().replace("J", "I")
    plaintext = input("Enter the plaintext to be encrypted: ").upper().replace("J", "I")
    
    # Validate that the plaintext contains only letters
    if not plaintext.isalpha():
        print("Plaintext must contain only letters.")
        return
    
    encrypted_text = playfair_encrypt(plaintext, key)
    print(f"Encrypted Text: {encrypted_text}")
    
    decrypted_text = playfair_decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
