import string
from random import choices


def create_password(length=8, upper=False, lower=False, digits=False, puncs=False):

    letters = ''

    if upper:
        letters += string.ascii_uppercase

    if lower:
        letters += string.ascii_lowercase

    if digits:
        letters += string.digits

    if puncs:
        letters += string.punctuation

    if letters == '':
        letters = string.ascii_letters

    return ''.join(choices(letters, k=length))


if __name__ == '__main__':
    create_password()
