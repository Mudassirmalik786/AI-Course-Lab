# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:00:45 2024

@author: HST LAPTOP FOR SALE
"""

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(5))