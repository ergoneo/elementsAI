# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:40:12 2022

@author: Laurent
"""

def count11(seq):
   counter = 0
   size = len(seq)
   for nb in range(1, size):
        print(str(nb) + ' ' + str(seq[nb]))
        if seq[nb] == 1 and seq[nb-1] == 1:
            counter = counter + 1
    # define this function and return the number of occurrences as a number
   return counter

print(count11([0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0])) # this should print 2