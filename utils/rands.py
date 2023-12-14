import string
from random import SystemRandom
from django.utils.text import slugify


def radon_letters(k=5):
    return ''.join(SystemRandom().choice(
        string.ascii_lowercase + string.dgits,
        k=k
    ))
    
def slugfy_new(text):
    return slugify(text)+ '-' + radon_letters(5)