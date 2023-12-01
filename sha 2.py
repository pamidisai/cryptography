import hashlib

def sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    hashed_text = sha256.hexdigest()
    return hashed_text

# Get input from the user
user_input = input("Enter text to hash using SHA-256: ")

hashed_result = sha256_hash(user_input)
print("Text:", user_input)
print("SHA-256 Hash:", hashed_result)
