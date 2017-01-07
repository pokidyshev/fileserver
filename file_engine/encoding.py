ALPHABET = 'mn6j2c4rv8bpygw95z7hsdaetxuk3fq'
BASE = len(ALPHABET)
MAPPING = list(reversed(range(BASE)))


# shuffle the bits and change the base
def encode(n):
    code = 0
    for i, b in enumerate(MAPPING):
        b1 = 1 << i
        b2 = 1 << MAPPING[i]
        if n & b1:
            code |= b2
    return enbase(code)


# go back to base 10 and unshuffle the bits
def decode(s):
    n = debase(s)
    result = 0
    for i, b in enumerate(MAPPING):
        b1 = 1 << i
        b2 = 1 << MAPPING[i]
        if n & b2:
            result |= b1
    return result


# change the base
def enbase(x):
    x = int(x)
    if x < BASE:
        return ALPHABET[x]
    return enbase(x / BASE) + ALPHABET[x % BASE]


# go back to base 10
def debase(x):
    result = 0
    for i, c in enumerate(reversed(x)):
        result += ALPHABET.index(c) * (BASE**i)
    return result
