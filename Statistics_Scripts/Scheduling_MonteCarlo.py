# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:48:31 2024

@author: Fulvio Raddi
"""

import numpy as np
import matplotlib.pyplot as plt


sims = 1000000

A = np.random.uniform(1,5,sims)
B = np.random.uniform(2,6,sims)

duration = A + B

# plt.figure(figsize = (3, 1.5))
plt.hist(duration, density = True)
plt.axvline(9, color = 'r')
plt.show()

print((duration > 9).sum()/sims)
