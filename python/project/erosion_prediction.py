"""
This code is designed to predict the future erosion rates of the remediated ravine at Hawthorn Hollow
"""
__author__ = "Rileigh Smith-Hopkins"

import numpy as np
import matplotlib.pyplot as plt
from data import value_sets

def plot_transect_data(weeks, values_set, transect_name):
    """
    Plot the transect data with best-fit lines and fill-between for slope error.

    Parameters:
    weeks (np.array): Array of weeks.
    values_set (np.array): 2D array of values for each dataset.
    transect_name (str): Name of the transect.
    """
    fits = [np.polyfit(weeks, values, 1, full=True) for values in values_set]
    year = np.linspace(1, 52)
    best_fits = [np.polyval(fit[0], year) for fit in fits]

    line_styles = ['-', '--', '-.', ':'] * 2
    colors = ['b', 'r', 'g', 'm', 'c', 'y', 'k', 'orange']

    plt.figure(figsize=(12, 7))

    for index, (values, best_fit) in enumerate(zip(values_set, best_fits)):
        plt.plot(weeks, values, marker='o', linestyle=line_styles[index], color=colors[index],
                 label=f"{transect_name} plot {index + 1}")
        plt.plot(year, best_fit, linestyle=line_styles[index], color=colors[index],
                 label=f"Best Fit {index + 1}")

        if transect_name == "USL":
            slope_error = 0.1
            plt.fill_between(year, best_fit - slope_error, best_fit + slope_error,
                             color=colors[index], alpha=0.2)

    plt.xlabel('Weeks', fontsize=14)
    plt.ylabel('Inches', fontsize=14)
    plt.title(f'{transect_name} Plot Data Predicted to 52 Weeks', fontsize=16)
    plt.xticks(weeks)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.ylim(0, 6)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    weeks = np.array(list(range(1, 11)))
    for transect in value_sets:
        plot_transect_data(weeks, value_sets[transect], transect)



