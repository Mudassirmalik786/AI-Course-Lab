# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:22:24 2024

@author: HST LAPTOP FOR SALE
"""

def lcs_recursive(str1, str2, m, n):
    if m == 0 or n == 0:
        return 0
    if str1[m-1] == str2[n-1]:
        return 1 + lcs_recursive(str1, str2, m-1, n-1)
    else:
        return max(lcs_recursive(str1, str2, m, n-1), lcs_recursive(str1, str2, m-1, n))
