import argparse
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
    parser = argparse.ArgumentParser(description='Password Generator')
    parser.add_argument('length', type=int, help='Length of Password')
    parser.add_argument(
        '-u', '--upper',  help='UpperCase Letters', action='store_true')
    parser.add_argument(
        '-l', '--lower',  help='LowerCase Letters', action='store_true')
    parser.add_argument(
        '-d', '--digit',  help='Digit Letters', action='store_true')
    parser.add_argument(
        '-p', '--punc',  help='Pucntuation Letters', action='store_true')

    args = parser.parse_args()

    create_password(args.length, args.upper,
                    args.lower, args.digit, args.punc)
