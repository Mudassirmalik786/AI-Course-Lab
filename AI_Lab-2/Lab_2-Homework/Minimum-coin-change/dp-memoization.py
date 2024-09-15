# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:18:53 2024

@author: HST LAPTOP FOR SALE
"""

def min_coins_memoization(coins, amount, memo=None):
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        res = min_coins_memoization(coins, amount - coin, memo)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    
    memo[amount] = min_coins
    return min_coins if min_coins != float('inf') else -1
