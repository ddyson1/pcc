#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:40:21 2019

@author: devindyson
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk and plot the points.
	rw = RandomWalk(5000)
	rw.fill_walk()
    
        # Set the size of the plotting window.
        plt.figure(dpi=128, figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.PuBuGn,
		edgecolor='none', s=5)

	# Emphasize the first and last points.
	plt.scatter(0, 0, c='green', edgecolor='none', s=15)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=15)

	# Remove the axes.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
    
	plt.show()

	keep_running = raw_input("Make another walk? (y/n): ")
	if keep_running.lower() == 'n':
		break