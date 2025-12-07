"""
Lab 15: Plot Other Graphs
Gavin Kidd
12/6/2025
This program uses matplotlib to plot various graphs
"""
import matplotlib.pyplot as plt
import numpy as np

def infinity_plot():
    s = 2
    t = np.linspace(0, 2*np.pi, 1000)

    x = np.power(np.cos(t), s) * np.cos(t)
    y = np.power(np.cos(t), s) * np.sin(t)

    fig, ax = plt.subplots()
    ax.plot(x, y, lw=3)
    plt.show()

def chevron():
    x = [1, 3, 8, 4, 3, 1]
    y = [1, 9, 2, 4, 3, 1]

    plt.plot(x, y)
    plt.show()

def heart():
    t = np.linspace(0, 2*np.pi, 1000)

    x = 16 * np.sin(t)**3
    y = 16 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    plt.plot(x, y)
    plt.show()

class Main:
    plot_map = {
        1: infinity_plot,
        2: chevron,
        3: heart
    }

    print("Welcome to my cool graphs! Pick the number of the graph you would like to see!")
    print(f"1: Infinity Symbol")
    print(f"2: Chevron Symbol")
    print(f"3: Heart Symbol")
    user_input = int(input("Enter the number of the shape you want: "))

    if user_input in plot_map:
        plot_map[user_input]()
    else:
        print("invalid input")

if __name__ == "__main__":
    Main()

