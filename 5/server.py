import socket
from Crypto.Cipher import DES
import base64

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as enc_file:
        encrypted_text_base64 = enc_file.read()

    encrypted_text = base64.b64decode(encrypted_text_base64)
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = des.decrypt(encrypted_text).decode('utf-8')

    with open(output_file, 'w') as dec_file:
        dec_file.write(decrypted_text.strip())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)
print("Server is listening on port 9999...")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

with open('received_encrypted_file.txt', 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)

print("Encrypted file received.")

key = b'8bytekey'
decrypt_file('received_encrypted_file.txt', 'decrypted_file.txt', key)
print("File decrypted successfully.")

client_socket.close()
server_socket.close()
