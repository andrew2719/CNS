def prepare_text(text):
    text = ''.join(filter(str.isalpha, text.upper()))
    text = text.replace('J', 'I')
    return text

def create_matrix(key):
    key = prepare_text(key)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = []
    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)
    print("Matrix: ", matrix)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_pair(matrix, a, b):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5], matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a], matrix[(row_b + 1) % 5][col_b]
    else:
        return matrix[row_a][col_b], matrix[row_b][col_a]

def decrypt_pair(matrix, a, b):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5], matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a], matrix[(row_b - 1) % 5][col_b]
    else:
        return matrix[row_a][col_b], matrix[row_b][col_a]

def playfair_encrypt(plaintext, key):
    matrix = create_matrix(key)
    plaintext = prepare_text(plaintext)
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a, b = encrypt_pair(matrix, plaintext[i], plaintext[i+1])
        ciphertext += a + b
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = create_matrix(key)
    ciphertext = prepare_text(ciphertext)
    
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a, b = decrypt_pair(matrix, ciphertext[i], ciphertext[i+1])
        plaintext += a + b
    
    return plaintext

# Example usage
key = "PLAYFAIR EXAMPLE"
plaintext = "HELLO WORLD"
encrypted = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(encrypted, key)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")