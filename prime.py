# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:54:15 2024

@author: virus
"""

def probability_of_even(a):
    c = 0
    total = len(a)
    for i in a:
        if i % 2 == 0:
            c = c + 1
    return c/total

def probability_of_prime(a):
    c = 0
    total = len(a)
    for i in a:
        if i > 1:
            c2 = 0
            for j in range(2,i):
                if i % j == 2:
                    c2 +=1
            if c2 == 0:
                c += 1
    return c / total

def probability_of_divisible(a):
    c = 0
    total = len(a)
    for i in a:
        if i % 15 == 0:
            c += 1
    return c/total






set_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 30, 11,15, 150]
print("The probability of choosing an even number would be:", probability_of_even(set_of_numbers))
print("The probability of choosing a prime number would be:", probability_of_prime(set_of_numbers))
print("The probability of choosing a number divisible by 3 an 5 would be:", probability_of_divisible(set_of_numbers))

