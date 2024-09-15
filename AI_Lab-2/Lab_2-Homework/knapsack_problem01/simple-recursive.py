# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:27:40 2024

@author: HST LAPTOP FOR SALE
"""

def knapsack_recursive(weights, values, W, n):
    if n == 0 or W == 0:
        return 0
    if weights[n-1] > W:
        return knapsack_recursive(weights, values, W, n-1)
    else:
        include_item = values[n-1] + knapsack_recursive(weights, values, W - weights[n-1], n-1)
        exclude_item = knapsack_recursive(weights, values, W, n-1)
        return max(include_item, exclude_item)
