#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:47:11 2019

@author: devindyson
"""

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=2)

# Set chart title and label axis. 
plt.title("Square Numbers",fontsize=18)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both',labelsize=14)

plt.show()