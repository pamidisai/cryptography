# Function to find modular multiplicative inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Function to encrypt text using affine cipher
def affine_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                encrypted_text += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using affine cipher
def affine_decrypt(text, a, b):
    decrypted_text = ""
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "Invalid 'a', no modular inverse exists."
    
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr(((a_inverse * (ord(char) - ord('a') - b)) % 26) + ord('a'))
            else:
                decrypted_text += chr(((a_inverse * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Get input from user
text = input("Enter the text to encrypt: ")
a = int(input("Enter the value of 'a' for encryption (must be coprime with 26): "))
b = int(input("Enter the value of 'b' for encryption: "))

encrypted_text = affine_encrypt(text, a, b)
print("Encrypted:", encrypted_text)

decrypted_text = affine_decrypt(encrypted_text, a, b)
print("Decrypted:", decrypted_text)
