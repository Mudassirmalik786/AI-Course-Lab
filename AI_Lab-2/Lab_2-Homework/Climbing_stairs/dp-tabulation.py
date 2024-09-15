# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:24:35 2024

@author: HST LAPTOP FOR SALE
"""

def climb_stairs_tabulation(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
