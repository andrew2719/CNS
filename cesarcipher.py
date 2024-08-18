def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Example usage
plain_text = "Hello, Zorld!"
shift = 3
encrypted_text = caesar_cipher_encrypt(plain_text, shift)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
