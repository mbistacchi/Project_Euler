# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:21:54 2019

@author: MSI Gaming
"""

"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def sum_factorial_digits(n):
    string = str(factorial(n))
    array = [int(i) for i in string]
    return sum(array)
