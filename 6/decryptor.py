# server.py

import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Configuration
SERVER_HOST = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 65432       # Arbitrary non-privileged port
BUFFER_SIZE = 4096        # Receive buffer size
RECEIVED_ENCRYPT_FILE = 'received_encrypt.txt'
OUTPUT_FILE = 'decrypted_output.txt'

# AES Configuration
AES_KEY = b'This is a key123'  # 16-byte key for AES-128
AES_IV = b'This is an IV456'   # 16-byte IV

def decrypt_data(encrypted_data):
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER_HOST, SERVER_PORT))
        s.listen(1)
        print(f"[*] Server listening on {SERVER_HOST}:{SERVER_PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"[*] Connected by {addr}")
            encrypted_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                encrypted_data += data

            print("[*] Encrypted data received. Saving to file...")
            with open(RECEIVED_ENCRYPT_FILE, 'wb') as f:
                f.write(encrypted_data)
            print(f"[*] Encrypted data saved to {RECEIVED_ENCRYPT_FILE}")

            print("[*] Decrypting data...")
            try:
                decrypted_data = decrypt_data(encrypted_data)
                with open(OUTPUT_FILE, 'wb') as f:
                    f.write(decrypted_data)
                print(f"[*] Decrypted data saved to {OUTPUT_FILE}")
            except (ValueError, KeyError) as e:
                print(f"[!] Decryption failed: {e}")

if __name__ == "__main__":
    start_server()
