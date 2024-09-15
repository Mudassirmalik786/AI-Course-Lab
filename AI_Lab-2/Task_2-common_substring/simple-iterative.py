# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:12:55 2024

@author: HST LAPTOP FOR SALE
"""

def longest_common_substring_iterative(s1, s2):
    max_length = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            length = 0
            while i + length < len(s1) and j + length < len(s2) and s1[i + length] == s2[j + length]:
                length += 1
            max_length = max(max_length, length)
    return max_length

print(longest_common_substring_iterative("ABCDF", "ACBCF"))