# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:14:29 2024

@author: HST LAPTOP FOR SALE
"""

def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]
