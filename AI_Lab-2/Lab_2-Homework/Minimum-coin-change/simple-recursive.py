# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:18:52 2024

@author: HST LAPTOP FOR SALE
"""

def min_coins_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        res = min_coins_recursive(coins, amount - coin)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    
    return min_coins if min_coins != float('inf') else -1
