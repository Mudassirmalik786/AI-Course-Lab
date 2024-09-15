# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:45:39 2024

@author: HST LAPTOP FOR SALE
"""

def depth(expr):
    if not isinstance(expr, (list, tuple)):
        return 0
    return 1 + max(depth(sub_expr) for sub_expr in expr)


print(depth('x'))  
print(depth(('expt', 'x', 2)))  
print(depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))  
print(depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))
