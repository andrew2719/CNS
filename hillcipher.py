# Python3 code to implement Hill Cipher
import numpy as np

keyMatrix = [[0] * 3 for i in range(3)]
# Generate vector for the message
messageVector = [[0] for i in range(3)]
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]

# Following function generates the key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    print("Key Matrix: ", keyMatrix)
    # print(keyMatrix)


# Following function encrypts the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

    print("Cipher Matrix: ", cipherMatrix)

# Function to decrypt the message
def decrypt(cipherVector):

# Calculate the determinant of A (det(A))
# Find the modular multiplicative inverse of det(A) mod 26
# Calculate the adjugate matrix of A
# Multiply the adjugate by the modular inverse of the determinant, mod 26

    # Find the modular multiplicative inverse of the determinant
    det = int(np.linalg.det(keyMatrix))
    print("Determinant: ", det)
    det_inv = pow(det, -1, 26)
    print("Determinant Inverse: ", det_inv)

    # Find the adjugate matrix
    adjugate = np.round(det * np.linalg.inv(keyMatrix)).astype(int) % 26
    print("Adjugate: ", adjugate)
    
    # Calculate the inverse key matrix
    inverse_key = (det_inv * adjugate) % 26
    print("Inverse Key: ", inverse_key)
    
    # Decrypt the message
    decrypted = np.dot(inverse_key, cipherVector) % 26

    return decrypted

def HillCipher(message, key):
    # Get key matrix from the key string
    getKeyMatrix(key)
    
    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    print("Message Vector: ", messageVector)
    
    # Following function generates the encrypted vector
    encrypt(messageVector)
    
    # Generate the encrypted text from the encrypted vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    
    # Print the ciphertext
    print("Ciphertext: ", "".join(CipherText))
    
    # Decrypt the message
    decrypted_vector = decrypt(np.array([cipherMatrix[i][0] for i in range(3)]))
    
    # Convert the decrypted vector back to text
    DecryptedText = []
    for i in range(3):
        DecryptedText.append(chr(int(decrypted_vector[i]) + 65))
    
    # Print the decrypted text
    print("Decrypted text: ", "".join(DecryptedText))

# Driver Code
def main():
    # Get the message to be encrypted
    message = "ACT"
    # Get the key
    key = "GYBNQKURP"
    HillCipher(message, key)

if __name__ == "__main__":
    main()

# This code is contributed by Pratik Somwanshi and modified to include decryption