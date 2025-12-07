"""
Lab 15: Plot Other Graphs
Gavin Kidd
12/6/2025
This program uses matplotlib to plot various graphs
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

