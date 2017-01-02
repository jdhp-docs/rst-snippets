#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Build datas ###############

x = np.arange(-10, 10, 0.01)
y = np.sin(2. * 2. * np.pi * x) * 1. / np.sqrt(2. * np.pi) * np.exp(-(x**2.)/2.)

# Plot data #################

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)

ax.plot(x, y, "-", label="Test")

# Set title and labels ######

ax.set_title(r"Test", fontsize=20)
ax.set_xlabel(r"$x$", fontsize=12)
ax.set_ylabel(r"$f(x)$", fontsize=12)

# Set legend ################

ax.legend(loc='lower right', fontsize=20)

# Save file #################

plt.savefig("plot2d.py.png")
