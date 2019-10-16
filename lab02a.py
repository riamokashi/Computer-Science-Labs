#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:36:12 2019

@author: riamokashi
"""


odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0





while True:
    n_str = input("Input an integer (0 terminates): ")
    n_int = int(n_str)
    if n_int == 0:
        break
    elif n_int < 0:
        continue
    elif n_int % 2 == 1:
        odd_sum += n_int
        odd_count += 1
    elif n_int % 2 == 0:
        even_sum += n_int
        even_count += 1
    positive_int_count += 1
    

    
        

# Good stuff goes here

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)