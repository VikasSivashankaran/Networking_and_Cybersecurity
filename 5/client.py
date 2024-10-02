import socket
from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        plaintext = file.read()

    padded_text = pad(plaintext)
    des = DES.new(key, DES.MODE_ECB)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    encrypted_text_base64 = base64.b64encode(encrypted_text)

    with open(output_file, 'wb') as enc_file:
        enc_file.write(encrypted_text_base64)

key = b'8bytekey'
encrypt_file('original_file.txt', 'encrypted_file.txt', key)
print("File encrypted successfully.")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))
print("Connected to the server.")

with open('encrypted_file.txt', 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)

print("Encrypted file sent.")
client_socket.close()
