#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:17:21 2019

@author: devindyson
"""
import matplotlib.pyplot as plt

x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Greens,edgecolor='none',s=10)

# set chart title and axis labels 
plt.title("Cubed Numbers", fontsize=18)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Values",fontsize=14)

# set size of tick labels 
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
