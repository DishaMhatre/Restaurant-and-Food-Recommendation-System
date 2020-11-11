# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:09:31 2020

@author: Admin
"""

from surprise import AlgoBase
from surprise import PredictionImpossible

import math
import numpy as np
import heapq

class similarity(AlgoBase):
    inputCuisines=input('Enter cuisines separated by commas: \n')
    list = inputCuisines.split (",")
    li = []
    for i in list:
    	li.append((i))
    print(li)
def cmp(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]
c=input('a')
d=input('b')
print(cmp(c,d))