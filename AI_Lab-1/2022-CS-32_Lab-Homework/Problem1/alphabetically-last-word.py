# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:51:32 2024

@author: HST LAPTOP FOR SALE
"""

def findAlphabeticallyLastWord(sentence):
    words = sentence.lower().replace("?", "").replace(".", "").replace(",", "").split()
    return max(words)

print(findAlphabeticallyLastWord("What is the last word in this sentence?"))
