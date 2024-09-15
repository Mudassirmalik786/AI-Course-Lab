# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:17:21 2024

@author: HST LAPTOP FOR SALE
"""

def min_coins_iterative(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1
