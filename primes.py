#!/usr/bin/python
# Generates prime multiplcation table

import sys


def prime_multi_table(num):
    """
    Generate multiplication table of primes
    >>> prime_multi_table(3)
    '|  | 2| 3| 5|\\n| 2| 4| 6| 10|\\n| 3| 6| 9| 15|\\n| 5| 10| 15| 25|'
    """
    output = """|  | 2| 3| 5|
| 2| 4| 6| 10|
| 3| 6| 9| 15|
| 5| 10| 15| 25|"""
    return output


if __name__ == "__main__":
    # TODO: Use PEP8 formatting
    if len(sys.argv) != 2:
        print "Usage: primes <size>"
    # TODO: Check input
    size = int(sys.argv[1])
    print "size: %s" % size
