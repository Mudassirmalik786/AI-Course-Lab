# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:17:20 2024

@author: HST LAPTOP FOR SALE
"""

def longest_common_substring_recursive(s1, s2, i=0, j=0, count=0):
    if i == len(s1) or j == len(s2):
        return count
    if s1[i] == s2[j]:
        count = longest_common_substring_recursive(s1, s2, i + 1, j + 1, count + 1)
    return max(count, longest_common_substring_recursive(s1, s2, i + 1, j, 0), 
                      longest_common_substring_recursive(s1, s2, i, j + 1, 0))


print(longest_common_substring_recursive("ABCDF", "ACDCF"))