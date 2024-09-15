# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:14:29 2024

@author: HST LAPTOP FOR SALE
"""

def fibonacci_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
