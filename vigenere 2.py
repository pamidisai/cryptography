def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = key[i % key_length]
            if shift.islower():
                shift = ord(shift) - ord('a')
            else:
                shift = ord(shift) - ord('A')
            
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = key[i % key_length]
            if shift.islower():
                shift = ord(shift) - ord('a')
            else:
                shift = ord(shift) - ord('A')
            
            if char.islower():
                decrypted_text += chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            else:
                decrypted_text += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text
text = input("Enter the text to encrypt: ")
key = input("Enter the key: ")

encrypted_text = vigenere_encrypt(text, key)
print("Encrypted:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
