# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:50:01 2019

@author: MSI Gaming
"""

"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

ans = sum(int(i) for i in str(2**1000))