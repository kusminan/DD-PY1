from random import sample
from string import ascii_letters
from string import digits


def get_random_password(n=8) -> str:
    random_pool = ascii_letters + digits
    return ''.join(sample(random_pool, n))


print(get_random_password())
