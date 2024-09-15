# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:30:13 2024

@author: HST LAPTOP FOR SALE
"""

def rod_cutting_recursive(price, n):
    if n == 0:
        return 0

    max_value = float('-inf')

    for i in range(n):
        max_value = max(max_value, price[i] + rod_cutting_recursive(price, n - i - 1))
    
    return max_value
