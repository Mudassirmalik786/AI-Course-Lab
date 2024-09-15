# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:24:35 2024

@author: HST LAPTOP FOR SALE
"""

def climb_stairs_memoization(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = climb_stairs_memoization(n-1, memo) + climb_stairs_memoization(n-2, memo)
    return memo[n]
