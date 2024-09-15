# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:18:54 2024

@author: HST LAPTOP FOR SALE
"""

def min_coins_tabulation(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
