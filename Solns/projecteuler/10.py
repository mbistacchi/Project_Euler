# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:57:10 2019

@author: MSI Gaming
"""

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
from itertools import islice, count
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    # count through a generator of all odd numbers to max possible divisor
    for number in islice(count(3, 2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

N = 2 * 10**6
primes = []
for i in range(0, N-1):
    if isPrime(i):
        primes.append(i)

print(sum(primes))