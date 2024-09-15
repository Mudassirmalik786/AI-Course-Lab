# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:14:28 2024

@author: HST LAPTOP FOR SALE
"""

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
