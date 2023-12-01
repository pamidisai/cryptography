# Padding function to ensure the plaintext length is a multiple of block size
def pad(plaintext, block_size):
    padding_length = block_size - len(plaintext) % block_size
    padding = bytes([padding_length]) * padding_length
    return plaintext + padding

# XOR operation for bytes
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# CBC encryption
def cbc_encrypt(plaintext, key, iv):
    block_size = len(key)
    plaintext = pad(plaintext, block_size)
    ciphertext = b""
    previous_block = iv

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        xored_block = xor_bytes(block, previous_block)
        encrypted_block = xor_bytes(xored_block, key)
        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext

# CBC decryption
def cbc_decrypt(ciphertext, key, iv):
    block_size = len(key)
    plaintext = b""
    previous_block = iv

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        decrypted_block = xor_bytes(block, key)
        plaintext += xor_bytes(decrypted_block, previous_block)
        previous_block = block

    # Remove padding
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]

    return plaintext

# Example usage
plaintext = b"Secret message to encrypt using CBC mode"
key = b"ThisIsA16ByteKey"
iv = b"RandomIV12345678"

encrypted_text = cbc_encrypt(plaintext, key, iv)
decrypted_text = cbc_decrypt(encrypted_text, key, iv)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
