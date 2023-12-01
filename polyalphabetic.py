def vigenere_cipher(text, key):
    text = text.upper()
    key = key.upper()

    encrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char) - 65) + (ord(key[key_index % len(key)]) - 65)) % 26 + 65)
            encrypted_text += shifted
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

# Get input from the user
plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")

encrypted = vigenere_cipher(plaintext, keyword)
print("Original:", plaintext)
print("Encrypted:", encrypted)
