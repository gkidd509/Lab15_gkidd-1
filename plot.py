"""
Lab 15: Plot Other Graphs
Gavin Kidd
12/6/2025
This program uses matplotlib to plot various graphs
"""
import matplotlib.pyplot as plt
import numpy as np

S = 2
t = np.linspace(0, 2*np.pi, 1000)

x = np.power(np.cos(t), S) * np.cos(t)
y = np.power(np.cos(t), S) * np.sin(t)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

