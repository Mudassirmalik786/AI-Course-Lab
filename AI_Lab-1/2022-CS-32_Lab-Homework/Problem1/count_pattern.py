# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:17:10 2024

@author: HST LAPTOP FOR SALE
"""

def count_pattern(pattern, lst):
    count = 0
    pattern_length = len(pattern)

    for i in range(len(lst) - pattern_length + 1):
        if tuple(lst[i:i + pattern_length]) == pattern:
            count += 1

    return count


print(count_pattern(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')))  
print(count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')))  
