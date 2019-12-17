# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:03:03 2019

@author: MSI Gaming
"""

"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
import numpy as np

numbers = np.arange(1, 101)
num_squared = numbers ** 2
num_sum = np.sum(numbers)
num_squared_sum = np.sum(num_squared)
print(num_squared_sum - num_sum**2)