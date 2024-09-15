# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:23:44 2024

@author: HST LAPTOP FOR SALE
"""

def climb_stairs_iterative(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
