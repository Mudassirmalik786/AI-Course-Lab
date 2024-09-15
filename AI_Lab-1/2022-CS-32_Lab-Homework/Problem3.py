# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:58:24 2024

@author: HST LAPTOP FOR SALE
"""

def tree_ref(tree, index_list):
    leaf = tree
    for i in index_list:
        leaf = leaf[i]
    return leaf

tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))

print(tree_ref(tree, [3, 1]))  
print(tree_ref(tree, [1, 1, 1]))  
print(tree_ref(tree, [0]))  
