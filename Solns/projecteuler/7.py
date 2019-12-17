# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:07:13 2019

@author: MSI Gaming
"""

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

from math import sqrt
from itertools import count, islice, takewhile

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


Nth = 10001
while Nth > 1:
    for number in count(1, 2):
        if isPrime(number):
            Nth -= 1
            if Nth == 1:
                ans = number
                break
            
            
        


