# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:27:40 2024

@author: HST LAPTOP FOR SALE
"""

def knapsack_memoization(weights, values, W, n, memo=None):
    if memo is None:
        memo = {}
    if (W, n) in memo:
        return memo[(W, n)]
    if n == 0 or W == 0:
        return 0
    if weights[n-1] > W:
        memo[(W, n)] = knapsack_memoization(weights, values, W, n-1, memo)
    else:
        include_item = values[n-1] + knapsack_memoization(weights, values, W - weights[n-1], n-1, memo)
        exclude_item = knapsack_memoization(weights, values, W, n-1, memo)
        memo[(W, n)] = max(include_item, exclude_item)
    return memo[(W, n)]
