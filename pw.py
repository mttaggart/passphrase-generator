from random import choice, randint

NOUNFILE = "wordlists/nouns.txt"
ADJFILE = "wordlists/adjectives.txt"

nouns = []
adjectives = []

def load_list(word_file, word_list):
    with open(word_file) as f:
        lines = f.readlines()
        for l in lines:
            word_list.append(l.rstrip())

load_list(NOUNFILE, nouns)
load_list(ADJFILE, adjectives)

def generate_password(sep=" ", digit_min=10, digit_max=99):
    return "{}{}{}_{}".format(
        choice(adjectives),
        sep,
        choice(nouns),
        randint(digit_min,digit_max)
    )

def password_list(n, sep=" ", digit_min=10, digit_max=99):
    pws = []
    for i in range(n):
        pws.append(generate_password(sep=sep, digit_min=digit_min, digit_max=digit_max))
    return pws