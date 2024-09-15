# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:18:23 2024

@author: HST LAPTOP FOR SALE
"""

def longest_common_substring_memo(s1, s2):
    memo = {}
    
    def helper(i, j, count):
        if i == len(s1) or j == len(s2):
            return count
        if (i, j, count) in memo:
            return memo[(i, j, count)]
        if s1[i] == s2[j]:
            count = helper(i + 1, j + 1, count + 1)
        memo[(i, j, count)] = max(count, helper(i + 1, j, 0), helper(i, j + 1, 0))
        return memo[(i, j, count)]
    
    return helper(0, 0, 0)

print(longest_common_substring_memo("ABCDF", "ACDCF"))