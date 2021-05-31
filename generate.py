import string
import random


def generate_password(length=10, capitals=False, especial=False):
    min_length = 10
    especial_chars = '!@#$%&'

    # the minimum number of characters has to be 10
    if length < min_length:
        length = min_length

    if capitals and especial:
        password = ''.join(random.choices(string.ascii_letters + string.digits + especial_chars, k=length))
    elif especial:
        password = ''.join(random.choices(string.ascii_lowercase + string.digits + especial_chars, k=length))
    elif capitals:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    else:
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    return password
