# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:24:34 2024

@author: HST LAPTOP FOR SALE
"""

def climb_stairs_recursive(n):
    if n <= 1:
        return 1
    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)
