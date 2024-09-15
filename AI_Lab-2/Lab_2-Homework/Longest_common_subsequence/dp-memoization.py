# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:22:25 2024

@author: HST LAPTOP FOR SALE
"""

def lcs_memoization(str1, str2, m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if str1[m-1] == str2[n-1]:
        memo[(m, n)] = 1 + lcs_memoization(str1, str2, m-1, n-1, memo)
    else:
        memo[(m, n)] = max(lcs_memoization(str1, str2, m, n-1, memo), lcs_memoization(str1, str2, m-1, n, memo))
    return memo[(m, n)]
