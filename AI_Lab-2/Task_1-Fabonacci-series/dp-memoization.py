# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:03:46 2024

@author: HST LAPTOP FOR SALE
"""

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
