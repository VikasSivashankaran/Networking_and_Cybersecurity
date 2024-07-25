import numpy as np

def getKeyMatrix(key, size):
    keyMatrix = np.zeros((size, size), dtype=int)
    k = 0
    for i in range(size):
        for j in range(size):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keyMatrix

def encrypt(messageVector, keyMatrix):
    size = len(keyMatrix)
    cipherMatrix = np.zeros((size, 1), dtype=int)
    for i in range(size):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(size):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
    return cipherMatrix

def HillCipher(message, key):
    size = int(len(key) ** 0.5)
    if size * size != len(key):
        print("Key length must be a perfect square.")
        return
    if len(message) % size != 0:
        print(f"Message length must be a multiple of {size}.")
        return

    keyMatrix = getKeyMatrix(key, size)
    messageVector = np.array([ord(char) % 65 for char in message]).reshape(size, 1)
    cipherMatrix = encrypt(messageVector, keyMatrix)
    CipherText = ''.join(chr(cipherMatrix[i][0] + 65) for i in range(size))
    print("Ciphertext: ", CipherText)

def main():
    message = input("Enter the message to be encrypted: ").upper().replace(" ", "")
    key = input("Enter the key (length should be a perfect square): ").upper().replace(" ", "")
    HillCipher(message, key)

if __name__ == "__main__":
    main()
