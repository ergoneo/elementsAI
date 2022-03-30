# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:51:19 2022

@author: Laurent
"""

import numpy as np


x = np.array([
             [25, 2, 50, 1, 500], 
             [39, 3, 10, 1, 1000], 
             [13, 2, 13, 1, 1000], 
             [82, 5, 20, 2, 120], 
             [130, 6, 10, 2, 600]
            ])   
y = np.array([127900, 222100, 143750, 268000, 460700])

c = np.linalg.lstsq(x, y)[0]
print(c)
print(x @ c)