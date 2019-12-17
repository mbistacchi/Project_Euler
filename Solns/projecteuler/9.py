# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:41:04 2019

@author: MSI Gaming
"""

"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

import math

def euclid_triple(n, m):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return a,b,c

max_nm = int(math.sqrt(1000))

for i in range(1, max_nm):
    for j in range(1, max_nm):
        a, b, c = euclid_triple(i, j)
        if a + b + c == 1000:
            print(a * b * c)