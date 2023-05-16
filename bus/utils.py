import random
import string


def generate_random_text() -> str:
    # Define the character set
    chars = string.ascii_uppercase + string.digits

    # Generate a random string of length 4
    random_text = "".join(random.choices(chars, k=4))

    return random_text
