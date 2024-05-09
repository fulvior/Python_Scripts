# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:26:16 2024

@author: Fulvio Raddi
"""

import random
import matplotlib.pyplot as plt
import numpy as np


def coin_trial():
    
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
         heads +=1
    return heads


def simulate(n):
    trials = []
    for i in range(n):
        trials.append(coin_trial())
    return(sum(trials)/n)


x = range(1,1000)
y = [simulate(i) for i in x]
plt.plot(x, y, color='red')
plt.axhline(y=50, color='b', linestyle='-')
plt.show() 