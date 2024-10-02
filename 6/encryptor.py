# client.py

import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Configuration
SERVER_HOST = '127.0.0.1'  # Replace with server's IP if different
SERVER_PORT = 65432        # Must match the server's port
INPUT_FILE = 'input.txt'
ENCRYPTED_FILE = 'encrypt.txt'

# AES Configuration
AES_KEY = b'This is a key123'  # 16-byte key for AES-128
AES_IV = b'This is an IV456'   # 16-byte IV

def encrypt_data(data):
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    padded_data = pad(data, AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return encrypted

def send_encrypted_data(encrypted_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        print(f"[*] Connected to server {SERVER_HOST}:{SERVER_PORT}")
        s.sendall(encrypted_data)
        print("[*] Encrypted data sent successfully.")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Input file '{INPUT_FILE}' does not exist. Please create it and try again.")
        return

    try:
        with open(INPUT_FILE, 'rb') as f:
            plaintext = f.read()
        print(f"[*] Read {len(plaintext)} bytes from {INPUT_FILE}")

        encrypted_data = encrypt_data(plaintext)
        print(f"[*] Encrypted data size: {len(encrypted_data)} bytes")

        with open(ENCRYPTED_FILE, 'wb') as f:
            f.write(encrypted_data)
        print(f"[*] Encrypted data saved to {ENCRYPTED_FILE}")

        send_encrypted_data(encrypted_data)
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
