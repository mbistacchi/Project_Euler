# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 23:08:37 2019

@author: MSI Gaming
"""

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt, ceil
from itertools import count, islice


N = 600851475143

def isPrime(n):
    if n < 2:
        return False

    # count through a generator from 2 to max possible prime
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


def largest_prime(N):
    n = int(sqrt(N))
    if n % 2 == 0:
        n +=1
    for i in range(n, 0, -2):
        num = N % i
        if num == 0 and isPrime(i):
            return i
 
ans = largest_prime(N)           
print ans
print largest_prime(N)