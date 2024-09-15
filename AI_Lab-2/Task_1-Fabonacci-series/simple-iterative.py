# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:48:25 2024

@author: HST LAPTOP FOR SALE
"""

def fibonacci_iterative(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        current = prev2 + prev1
        prev2 = prev1
        prev1 = current
    return prev1

array = []
array = fibonacci_iterative(5)
print(array)