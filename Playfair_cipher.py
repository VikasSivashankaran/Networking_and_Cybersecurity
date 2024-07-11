def generate_key_square(key):
    # Create a 5x5 key square
    key_square = [['' for _ in range(5)] for _ in range(5)]
    used_chars = set()

    # Remove duplicates from the key and add the characters to the key square
    i = 0
    j = 0
    for char in key:
        if char not in used_chars and char != 'J':  # 'I' and 'J' are considered the same
            key_square[i][j] = char
            used_chars.add(char)
            j += 1
            if j == 5:
                i += 1
                j = 0

    # Fill the remaining cells with the rest of the alphabet
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # 'J' is excluded
        if char not in used_chars:
            key_square[i][j] = char
            used_chars.add(char)
            j += 1
            if j == 5:
                i += 1
                j = 0

    return key_square

def preprocess_message(message):
    # Remove spaces and convert to uppercase
    message = message.replace(' ', '').upper()
    message = message.replace('J', 'I')  # 'I' and 'J' are considered the same

    # Insert 'X' between repeated letters and at the end if the length is odd
    processed_message = ''
    i = 0
    while i < len(message):
        processed_message += message[i]
        if i + 1 < len(message) and message[i] == message[i + 1]:
            processed_message += 'X'
        else:
            i += 1
        i += 1
    if len(processed_message) % 2 != 0:
        processed_message += 'X'

    return processed_message

def find_position(char, key_square):
    for i, row in enumerate(key_square):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None

def encrypt_pair(pair, key_square):
    row1, col1 = find_position(pair[0], key_square)
    row2, col2 = find_position(pair[1], key_square)

    if row1 == row2:
        # Same row: shift columns to the right
        return key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column: shift rows down
        return key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
    else:
        # Rectangle: swap columns
        return key_square[row1][col2] + key_square[row2][col1]

def encrypt_message(message, key_square):
    encrypted_message = ''
    for i in range(0, len(message), 2):
        encrypted_message += encrypt_pair(message[i:i + 2], key_square)
    return encrypted_message

def playfair_encrypt(message, key):
    key_square = generate_key_square(key)
    processed_message = preprocess_message(message)
    encrypted_message = encrypt_message(processed_message, key_square)
    return encrypted_message

# Example usage
key = "MONARCHY"
message = "INSTRUMENTS"
encrypted_message = playfair_encrypt(message, key)
print(f"Key: {key}")
print(f"Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
