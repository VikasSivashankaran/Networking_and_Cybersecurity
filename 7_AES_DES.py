import time
import tracemalloc
from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
import os

def measure_des(file_path):
    key = get_random_bytes(8)  # DES requires an 8-byte key
    cipher = DES.new(key, DES.MODE_ECB)

    # Read file content
    with open(file_path, "rb") as f:
        data = f.read()

    # Measure encryption time and memory usage
    tracemalloc.start()
    start_time = time.time()
    ciphertext = cipher.encrypt(data.ljust((len(data) + 7) // 8 * 8, b'\0'))  # Padding data to be a multiple of 8 bytes
    encryption_time = time.time() - start_time
    _, peak_memory_encryption = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Measure decryption time and memory usage
    tracemalloc.start()
    start_time = time.time()
    plaintext = cipher.decrypt(ciphertext)
    decryption_time = time.time() - start_time
    _, peak_memory_decryption = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return encryption_time, decryption_time, peak_memory_encryption, peak_memory_decryption, len(ciphertext), ciphertext, plaintext

def measure_aes(file_path):
    key = get_random_bytes(16)  # AES requires a 16-byte key
    cipher = AES.new(key, AES.MODE_ECB)

    # Read file content
    with open(file_path, "rb") as f:
        data = f.read()

    # Measure encryption time and memory usage
    tracemalloc.start()
    start_time = time.time()
    ciphertext = cipher.encrypt(data.ljust((len(data) + 15) // 16 * 16, b'\0'))  # Padding data to be a multiple of 16 bytes
    encryption_time = time.time() - start_time
    _, peak_memory_encryption = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Measure decryption time and memory usage
    tracemalloc.start()
    start_time = time.time()
    plaintext = cipher.decrypt(ciphertext)
    decryption_time = time.time() - start_time
    _, peak_memory_decryption = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return encryption_time, decryption_time, peak_memory_encryption, peak_memory_decryption, len(ciphertext), ciphertext, plaintext

def main():
    # Path to the existing input file
    file_path = "7_AES_DES.txt"

    # Ensure the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # DES Evaluation
    des_enc_time, des_dec_time, des_mem_enc, des_mem_dec, des_output_size, des_ciphertext, des_plaintext = measure_des(file_path)
    print(f"DES Encryption Time: {des_enc_time:.6f} seconds")
    print(f"DES Decryption Time: {des_dec_time:.6f} seconds")
    print(f"DES Peak Memory Usage (Encryption): {des_mem_enc / 1024:.2f} KB")
    print(f"DES Peak Memory Usage (Decryption): {des_mem_dec / 1024:.2f} KB")
    print(f"DES Output Size: {des_output_size} bytes")
    print(f"DES Encrypted Message (Hex): {des_ciphertext[:100].hex()}... (truncated)")
    print(f"DES Decrypted Message: {des_plaintext[:100]}... (truncated)\n")

    # AES Evaluation
    aes_enc_time, aes_dec_time, aes_mem_enc, aes_mem_dec, aes_output_size, aes_ciphertext, aes_plaintext = measure_aes(file_path)
    print(f"AES Encryption Time: {aes_enc_time:.6f} seconds")
    print(f"AES Decryption Time: {aes_dec_time:.6f} seconds")
    print(f"AES Peak Memory Usage (Encryption): {aes_mem_enc / 1024:.2f} KB")
    print(f"AES Peak Memory Usage (Decryption): {aes_mem_dec / 1024:.2f} KB")
    print(f"AES Output Size: {aes_output_size} bytes")
    print(f"AES Encrypted Message (Hex): {aes_ciphertext[:100].hex()}... (truncated)")
    print(f"AES Decrypted Message: {aes_plaintext[:100]}... (truncated)\n")

if __name__ == "__main__":
    main()
