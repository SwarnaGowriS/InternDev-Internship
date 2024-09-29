import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for password length
password_length = int(input("Enter the desired password length: "))
# Generate the password
generated_password = generate_password(password_length)
# Display the password
print("Generated Password:", generated_password)