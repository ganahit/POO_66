# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 10:27:36 2025

@author: lab
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
