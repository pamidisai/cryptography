def columnar_encrypt(plaintext, key):
    # Calculate the number of rows required
    num_rows = (len(plaintext) + len(key) - 1) // len(key)

    # Create an empty matrix to hold the plaintext in columnar order
    matrix = [[' ' for _ in range(len(key))] for _ in range(num_rows)]

    # Fill the matrix with the plaintext characters
    index = 0
    for i in range(num_rows):
        for j in range(len(key)):
            if index < len(plaintext):
                matrix[i][j] = plaintext[index]
                index += 1

    # Arrange columns based on the key
    encrypted_text = ''
    for k in sorted(key):
        col = key.index(k)
        encrypted_text += ''.join(matrix[i][col] for i in range(num_rows))

    return encrypted_text

# Get user input
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (sequence of numbers indicating column order, e.g., '2314'): ")

# Remove spaces and non-numeric characters from the key
key = ''.join(filter(str.isdigit, key))

encrypted_message = columnar_encrypt(plaintext, key)
print("Encrypted message:", encrypted_message)
