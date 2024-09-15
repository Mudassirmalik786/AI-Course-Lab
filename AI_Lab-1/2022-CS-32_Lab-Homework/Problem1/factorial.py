# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:12:35 2024

@author: HST LAPTOP FOR SALE
"""

def factorial(n):
    facto = 1
    if not isinstance(n, int):
        raise TypeError("factorial cannot be obtained other than integers")
    if n > 0:
        for i in range(1, n + 1): 
            facto = facto * i
        
        return facto
    
    if n < 0:
        raise ValueError("factorial must be non negative")
    
    return facto

facto = factorial(1)
print(facto)