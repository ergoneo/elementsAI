# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:46:12 2022

@author: Laurent
"""

# input values for one mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbours

x = [66, 5, 15, 2, 500]
c = [3000, 200 , -50, 5000, 100]     # coefficient values

prediction = c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]

print(prediction)