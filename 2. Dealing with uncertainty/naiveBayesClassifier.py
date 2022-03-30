# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:44:53 2022

@author: Laurent
"""

def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    r = 2              #likelihood
    for i in range(n):
             odds = odds * r      # edit here to update the odds
    print(odds)

n = 5
flip(n)