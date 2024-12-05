import random
import string

def generate_password(length=12):
    """
    Generate a strong random password.
    
    Args:
        length (int): The length of the password. Default is 12.
        
    Returns:
        str: The generated password.
    """
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one character from each pool
    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)

#main
print("Generated Password:", generate_password())
