# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 23:36:17 2019

@author: MSI Gaming
"""

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

# 6 digit pals must be minimum 100 * 100, up to 999 * 999
# 

def split_num(num):
    return [int(d) for d in str(num)]


def check_palin(num):
    digits = split_num(num)
    i = 0
    while i < len(digits)/2:
        if digits[i] == digits[-(i+1)]:
            i += 1
        else:
            return False
    return True


N1 = range(999, 99, -1)
N2 = range(999, 99, -1)
ans = []
for i in N1:
    for j in N2:
        n = i * j
        if check_palin(n):
            ans.append(n)
print max(ans)