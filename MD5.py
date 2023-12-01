import hashlib

def md5_hash(text):
    # Create an MD5 hash object
    md5 = hashlib.md5()
    
    # Update the hash object with the input text
    md5.update(text.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash digest
    hashed_text = md5.hexdigest()
    
    return hashed_text

# Get input from the user
user_input = input("Enter text to hash using MD5: ")

hashed_result = md5_hash(user_input)
print("Text:", user_input)
print("MD5 Hash:", hashed_result)
