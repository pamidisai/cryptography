import binascii

# Initial permutation table for the key
initial_key_permutation = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

# Example 8-byte key
example_key = b"secretkey"

def generate_subkeys(key):
    # Perform the initial key permutation
    key_bits = ''.join(format(byte, '08b') for byte in key)
    permuted_key = ''.join(key_bits[i - 1] for i in initial_key_permutation)

    # Split the key into two halves
    left_half = permuted_key[:28]
    right_half = permuted_key[28:]

    subkeys = []
    for round_num in range(16):
        # Perform circular left shift on both halves
        left_half = left_half[1:] + left_half[0]
        right_half = right_half[1:] + right_half[0]

        # Combine the halves
        combined_key = left_half + right_half

        # Perform the key compression permutation
        round_key = ''.join(combined_key[i - 1] for i in [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4])
        subkeys.append(round_key)

    return subkeys

def main():
    # Get input from the user
    plaintext = input("Enter plaintext (8 bytes): ").encode('utf-8')
    key = input("Enter 8-byte key: ").encode('utf-8')

    # Check if the key is 8 bytes long
    if len(key) != 8:
        print("Key should be 8 bytes long!")
        return

    # Generate subkeys
    subkeys = generate_subkeys(key)

    # Display subkeys
    for i, subkey in enumerate(subkeys):
        print(f"Round {i + 1} Subkey: {subkey}")

if __name__ == "__main__":
    main()
