# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:27:41 2024

@author: HST LAPTOP FOR SALE
"""

def knapsack_tabulation(weights, values, W, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]
