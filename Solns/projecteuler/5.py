# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 00:05:16 2019

@author: MSI Gaming
"""


"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
    
    
def min_evenly_divis(num):
    
    guess = 2520
    i = 1
    while i < num:
        if guess % i == 0:
            if i == num:
                return(guess)
                
            i += 1   
        
        else:
                i = 1
                guess += 20
        
        
        #print("i is: %s", i)
        #print(guess)
    
print(min_evenly_divis(20))