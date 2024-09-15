# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:20:23 2024

@author: HST LAPTOP FOR SALE
"""

def rod_cutting_iterative(price, n):
    dp = [0] * (n + 1)

    # Build the dp table in bottom-up manner
    for i in range(1, n + 1):
        max_value = float('-inf')
        for j in range(i):
            max_value = max(max_value, price[j] + dp[i - j - 1])
        dp[i] = max_value
    
    return dp[n]

print(rod_cutting_iterative([1, 5, 8, 9, 10, 17, 17, 20], 8))