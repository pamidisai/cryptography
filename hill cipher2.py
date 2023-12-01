def getKeyMatrix():
    # Get the key matrix as a list of integers
    # This can be modified to obtain the key matrix in another way
    key = []
    for i in range(3):
        row = []
        for j in range(3):
            while True:
                try:
                    value = int(input(f"Enter the value for key[{i}][{j}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        key.append(row)
    return key

def getModularInverse(det):
    # Get the modular inverse of the determinant of the key matrix
    # This can be modified to obtain the modular inverse in another way
    while True:
        try:
            modular_inverse = int(input(f"Enter the modular inverse of the determinant {det}: "))
            return modular_inverse
        except ValueError:
            print("Invalid input. Please enter an integer.")

def encrypt(plaintext, key):
    # Encrypt the plaintext using the key matrix
    return [sum(a*b for a, b in zip(key_row, plaintext)) % 26 for key_row in key]

def decrypt(ciphertext, key, modular_inverse):
    # Decrypt the ciphertext using the inverse key matrix
    inverse_key = [[sum(a*b for a, b in zip(key_row, key_col)) % 26 for key_col in zip(*key)] for key_row in key]
    return [sum(a*b for a, b in zip(inverse_key_row, ciphertext)) % 26 for inverse_key_row in inverse_key]

def hill_cipher():
    # Get the key matrix
    key = getKeyMatrix()

    # Calculate the modular inverse of the determinant of the key matrix
    modular_inverse = getModularInverse(determinant(key))

    # Encrypt or decrypt the plaintext
    operation = input("Enter 'encrypt' to encrypt a plaintext message or 'decrypt' to decrypt a ciphertext message: ")
    if operation == 'encrypt':
        # Convert the plaintext into a sequence of integers
        plaintext = input("Enter the plaintext message: ")
        plaintext = [ord(c) - ord('A') for c in plaintext if c.isalpha()]

        # Encrypt the plaintext using the key matrix
        ciphertext = encrypt(plaintext, key)
        print("Ciphertext: ", ''.join(chr(ord('A') + i) for i in ciphertext))
    elif operation == 'decrypt':
        # Convert the ciphertext into a sequence of integers
        ciphertext = input("Enter the ciphertext message: ")
        ciphertext = [ord(c) - ord('A') for c in ciphertext if c.isalpha()]

        # Decrypt the ciphertext using the inverse key matrix
        decrypted_text = decrypt(ciphertext, key, modular_inverse)
        print("Decrypted text: ", ''.join(chr(ord('A') + i) for i in decrypted_text))
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")

hill_cipher()
