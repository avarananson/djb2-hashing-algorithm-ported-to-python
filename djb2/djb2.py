
import re


def hashed(str):

    if(type(str) == list):
        print(algo("".join(str)))
    else:
        print(algo(str))


def algo(val):
    hash = 5381

    for st in val:
        hash = (((hash << 5) + hash) + ord(st))

    return hash & 0xffffffffffffffff  # return 64 bit version
