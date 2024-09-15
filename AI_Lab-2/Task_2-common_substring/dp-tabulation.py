# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:19:26 2024

@author: HST LAPTOP FOR SALE
"""

def longest_common_substring_tabulation(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_length = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0

    return max_length

print(longest_common_substring_tabulation("ABCDF", "ACDCF"))