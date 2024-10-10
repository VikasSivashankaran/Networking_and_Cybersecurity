import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted_msg = [(ord(char) ** e) % n for char in plaintext]
    return encrypted_msg

def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted_msg = ''.join([chr((char ** d) % n) for char in ciphertext])
    return decrypted_msg

def rsa():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    if p == q:
        print("p and q must be distinct primes. Please try again.")
        return

    public_key, private_key = generate_keypair(p, q)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    message = input("Enter the message to encrypt: ")

    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

rsa()
