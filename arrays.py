# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:17:12 2024

@author: virus
"""

import numpy as np

numbers = np.array([10,10,10,20,30,40])

print(numbers[numbers != 10])

# numbers.extend([50,60])
# numbers.insert(0, 10)
# numbers.remove(10)
# numbers.pop(0)

# for number in numbers:
#     print(number)

# print("The array 'numbers' has length ", len(numbers))
# print("The first element of the array is ", numbers[0])
# print("The second element of the array is ", numbers[1])
# print("The third element of the array is ", numbers[2])