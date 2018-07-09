#!/usr/bin/python
# Generates prime multiplcation table

import sys
import math


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


def get_primes(n):
    """
    Use Sieve of Eratosthenes to find primes
    >>> get_primes(3)
    [2, 3, 5]
    >>> get_primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """
    # Estimate sieve size
    size = int(n*math.log(n) + n*math.log(n))
    sieve = [True] * size
    for i in range(2, int(math.sqrt(size)) + 1):
        pointer = i * 2
        while pointer < size:
            sieve[pointer] = False
            pointer += i

    primes = []

    for i in range(2, size):
        if sieve[i] == True:
            primes.append(i)
            # Stop when we get to nth prime
            if len(primes) == n:
                break
    return primes


def prime_multi_table(n):
    """
    Generate multiplication table of primes
    >>> prime_multi_table(3)
    '|  | 2| 3| 5|\\n| 2| 4| 6| 10|\\n| 3| 6| 9| 15|\\n| 5| 10| 15| 25|'
    """
    primes = get_primes(n)
    # TODO: generate table in more efficient/elegant way
    line = '|  |'
    for i in primes:
        line += " %s|" % i
    line += "\n|"
    for i in primes:
        line += " %s|" % i
        for j in primes:
            product = i*j
            line += " %s|" % product
        if j != i or i != primes[-1]:
            line += "\n|"
    return line


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: primes <n>"
        print "where n is number of primes"
    # TODO: Check input
    # TODO: Exception handling
    n = int(sys.argv[1])

    table = prime_multi_table(n)
    print table
