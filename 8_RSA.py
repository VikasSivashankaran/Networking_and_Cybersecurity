import random

# Helper function to compute GCD using Euclid's algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Helper function to compute modular inverse
def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

# Function to generate public and private keys
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = mod_inverse(e, phi)

    # Public key (e, n) and Private key (d, n)
    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert each letter in the plaintext to numbers based on the ASCII values
    encrypted_msg = [(ord(char) ** e) % n for char in plaintext]
    return encrypted_msg

# Function to decrypt a message
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Decrypt each number in the ciphertext back to letters
    decrypted_msg = ''.join([chr((char ** d) % n) for char in ciphertext])
    return decrypted_msg

# Function to take user inputs and run the RSA encryption-decryption process
def rsa():
    # Get prime numbers p and q from the user
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    # Ensure p and q are distinct
    if p == q:
        print("p and q must be distinct primes. Please try again.")
        return

    # Generate public and private keys
    public_key, private_key = generate_keypair(p, q)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Get the plaintext message from the user
    message = input("Enter the message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

# Run the RSA program
rsa()
