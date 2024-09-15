# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:14:26 2024

@author: HST LAPTOP FOR SALE
"""

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
