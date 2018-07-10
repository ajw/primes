#!/usr/bin/python
# Generates prime multiplcation table

from __future__ import print_function
import sys
import math


def get_primes(n):
    """
    Use Sieve of Eratosthene to find primes
    >>> get_primes(3)
    [2, 3, 5]
    >>> get_primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """
    # Use Rossers Theorem to get upper bound for nth prime.
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
    |  | 2| 3| 5|
    | 2| 4| 6| 10|
    | 3| 6| 9| 15|
    | 5| 10| 15| 25|
    """
    primes = get_primes(n)
    # TODO: generate table in more efficient/elegant way
    print ('|  |', end='')
    for i in primes:
        print(" %s|" % i, end='')
    print("\n|", end='')
    for i in primes:
        print (" %s|" % i, end='')
        for j in primes:
            product = i*j
            print (" %s|" % product, end='')
        if j != i or i != primes[-1]:
            print ("\n|", end='')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: primes <n>")
        print ("where n is number of primes")
    # TODO: Check input
    # TODO: Exception handling
    n = int(sys.argv[1])

    table = prime_multi_table(n)
    # print table
