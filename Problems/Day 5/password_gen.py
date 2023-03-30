import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
    # Define character sets to be used in password generation
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    # Create a list to hold the characters to be used in password generation
    chars = []

    # Add characters to the list based on user-specified criteria
    if include_uppercase:
        chars.extend(list(uppercase_chars))
    if include_lowercase:
        chars.extend(list(lowercase_chars))
    if include_digits:
        chars.extend(list(digit_chars))
    if include_symbols:
        chars.extend(list(symbol_chars))

    # Make sure the password contains at least one of each type of character
    if include_uppercase:
        chars.append(random.choice(uppercase_chars))
    if include_lowercase:
        chars.append(random.choice(lowercase_chars))
    if include_digits:
        chars.append(random.choice(digit_chars))
    if include_symbols:
        chars.append(random.choice(symbol_chars))

    # Shuffle the list to randomize the order of the characters
    random.shuffle(chars)

    # Generate the password by selecting characters from the shuffled list
    password = ''.join(chars[:length])

    return password

# Example usage:
password = generate_password(13, True, True, True, True)
print(password)
