"""
This code is designed to predict the future erosion rates of the remediated ravine at Hawthorn Hollow
"""
__author__ = "Rileigh Smith-Hopkins"

import matplotlib.pyplot as plt
import numpy as np

def transect_usl_best_fit_data():
    # Defining the data for each pin at transect USL
    weeks = np.array(list(range(1, 11)))  # 10 weeks (Week 1 to Week 10)
    values_set_1 = np.array([2, 2.25, 2.375, 3.0625, 2.625, 2.75, 2.75, 2.5, 2.1875, 3])
    values_set_2 = np.array([2, 2, 2, 1.875, 2, 2, 2.5, 2, 1.9375, 1.875])
    values_set_3 = np.array([2, 2.75, 3, 2.875, 2.875, 3, 3.875, 2.25, 2.75, 2.875])
    values_set_4 = np.array([2, 2.625, 2.5, 2.5, 2.75, 2.375, 2.75, 2.875, 2.875, 2.5])
    values_set = np.array([values_set_1, values_set_2, values_set_3, values_set_4])

    # Computing best-fit lines for each dataset
    fit_1 = np.polyfit(weeks, values_set_1, 1)  # Linear fit (degree 1)
    fit_2 = np.polyfit(weeks, values_set_2, 1)
    fit_3 = np.polyfit(weeks, values_set_3, 1)
    fit_4 = np.polyfit(weeks, values_set_4, 1)
    fits = []
    for values in values_set:
        fits.append(np.polyfit(weeks, values, 1))

  # Data to extrapolate to 52 weeks
    year = np.linspace(1, 52)
    # Values of Y for the best fit lines
    best_fit_1 = np.polyval(fit_1, year)
    best_fit_2 = np.polyval(fit_2, year)
    best_fit_3 = np.polyval(fit_3, year)
    best_fit_4 = np.polyval(fit_4, year)
    best_fits= []
    for fit in fits:
        best_fits.append(np.polyval(fit, year))
    # Create the plot
    plt.figure(figsize=(12, 7))
    colors = ['b', 'r', 'g', 'm', 'm', 'y', 'k']
    # plt.plot(weeks, values_set_1, marker='o', linestyle='-', color='b', label="USL plot 1")
    # plt.plot(year, best_fit_1, color='b', linestyle='--', label="Best Fit 1")
    #
    # plt.plot(weeks, values_set_2, marker='s', linestyle='--', color='r', label="USL plot 2")
    # plt.plot(year, best_fit_2, color='r', linestyle='--', label="Best Fit 2")
    #
    # plt.plot(weeks, values_set_3, marker='^', linestyle=':', color='g', label="USL plot 3")
    # plt.plot(year, best_fit_3, color='g', linestyle='--', label="Best Fit 3")
    #
    # plt.plot(weeks, values_set_4, marker='d', linestyle='-', color='m', label="USL plot 4")
    # plt.plot(year, best_fit_4, color='m', linestyle='--', label="Best Fit 4")
    for index, (values, best_fit) in enumerate(zip(values_set, best_fits)):
        plt.plot(year, best_fit, color=colors[index])
        plt.plot(weeks, values, color=colors[index])


    # Add labels and title
    plt.xlabel('Weeks')
    plt.ylabel('Inches')
    plt.title('Comparison of USL Plot Data Sets With Best Fit Lines')
    plt.xticks(weeks)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Adjust the y-axis to account for the 12 inches as total pin length
    plt.ylim(0, 6)  # Set the y-axis to range from 0 to 12

    # Plotting the graph with best fit lines
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    transect_usl_best_fit_data()

import matplotlib.pyplot as plt
import numpy as np

def transect_usr_best_fit_data():
    # Defining the data set for each pin at transect USR
    weeks = np.array(list(range(1, 11)))
    values_set_1 = np.array([2, 2.0625, 2.0625, 2.125, 2.0625, 2.125, 2.25, 2.25, 2, 2])
    values_set_2 = np.array([2, 2, 2.375, 2.5, 2.25, 2.5, 2.5, 2.5, 1.9375, 1.875])
    values_set_3 = np.array([2, 2.125, 1.9375, 2.125, 1.9375, 2.375, 2.25, 1.5, 1.75, 2.25])
    values_set_4 = np.array([2, 1.875, 1.75, 2, 2.0625, 1.875, 1.75, 1.875, 2.875, 1.875])

    # Computing best fit lines for each data set
    fit_1 = np.polyfit(weeks, values_set_1, 1)



#### RENAME from erosion_prediction.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization
