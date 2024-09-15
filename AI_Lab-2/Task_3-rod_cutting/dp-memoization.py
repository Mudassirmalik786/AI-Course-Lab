# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:31:12 2024

@author: HST LAPTOP FOR SALE
"""

def rod_cutting_memoization(price, n, memo=None):
    if memo is None:
        memo = [-1] * (n + 1)

    if n == 0:
        return 0

    if memo[n] != -1:
        return memo[n]

    max_value = float('-inf')

    for i in range(n):
        max_value = max(max_value, price[i] + rod_cutting_memoization(price, n - i - 1, memo))

    memo[n] = max_value
    return max_value
