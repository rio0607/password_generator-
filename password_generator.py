import random
import string

def generate_password():
    # Get user specifications
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special_characters = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Define character sets based on user preferences
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digit_characters = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user preferences
    all_characters = lowercase_letters
    if include_uppercase:
        all_characters += uppercase_letters
    if include_digits:
        all_characters += digit_characters
    if include_special_characters:
        all_characters += special_characters

    # Ensure the password has at least one character from each selected set
    password = [
        random.choice(lowercase_letters),
    ]
    if include_uppercase:
        password.append(random.choice(uppercase_letters))
    if include_digits:
        password.append(random.choice(digit_characters))
    if include_special_characters:
        password.append(random.choice(special_characters))

    # Fill the rest of the password with random characters
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the characters to make the password more random
    random.shuffle(password)

    # Convert the list of characters to a string
    generated_password = ''.join(password)

    return generated_password

# Example usage
password = generate_password()
print("Generated Password:", password)
