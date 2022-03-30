# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:48:32 2022

@author: Laurent
"""

import numpy as np

x = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100]])
c = np.array([3000, 200 , -50, 5000, 100])

print(x @ c)
