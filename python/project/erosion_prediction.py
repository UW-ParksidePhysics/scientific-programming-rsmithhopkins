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
    fits = [np.polyfit(weeks, values, 1) for values in values_set]

    # Data to extrapolate to 52 weeks
    year = np.linspace(1, 52)  # Default to 50 equally spaced points without specifying a number
    best_fits = [np.polyval(fit, year) for fit in fits]

    # Define distinct line styles and colors
    line_styles = ['-', '--', '-.', ':']  # Solid, dashed, dash-dot, dotted
    colors = ['b', 'r', 'g', 'm']  # Blue, red, green, magenta

    # Create the plot
    plt.figure(figsize=(12, 7))

    for index, (values, best_fit) in enumerate(zip(values_set, best_fits)):
        plt.plot(weeks, values, marker='o', linestyle=line_styles[index], color=colors[index],
                 label=f"USL plot {index + 1}")
        plt.plot(year, best_fit, linestyle=line_styles[index], color=colors[index],
                 label=f"Best Fit {index + 1}")

    # Add labels and title
    plt.xlabel('Weeks')
    plt.ylabel('Inches')
    plt.title('USL Plot Data Predicted to 52 Weeks')
    plt.xticks(weeks)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Adjust the y-axis to account for the 12 inches as total pin length
    plt.ylim(0, 6)  # Set the y-axis to range from 0 to 6

    # Plotting the graph with best fit lines
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    transect_usl_best_fit_data()

import matplotlib.pyplot as plt
import numpy as np

def transect_usr_best_fit_data():
    # Defining the data for each pin at transect USR
    weeks = np.array(list(range(1, 11)))  # 10 weeks (Week 1 to Week 10)

    values_set_1 = np.array([2, 2.0625, 2.0625, 2.125, 2.0625, 2.125, 2.25, 2.25, 2.375, 2.3333])
    values_set_2 = np.array([2, 2, 2.375, 2.5, 2.25, 2.5, 2.5, 2.5, 1.9375, 1.875])
    values_set_3 = np.array([2, 2.125, 1.9375, 2.125, 1.9375, 2.375, 2.25, 1.5, 1.75, 2.25])
    values_set_4 = np.array([2, 1.875, 1.75, 2, 2.0625, 1.875, 1.75, 1.875, 2.875, 1.875])
    values_set = np.array([values_set_1, values_set_2, values_set_3, values_set_4])

    # Computing best-fit lines for each dataset
    fits = [np.polyfit(weeks, values, 1) for values in values_set]

    # Data to extrapolate to 52 weeks
    year = np.linspace(1, 52)
    best_fits = [np.polyval(fit, year) for fit in fits]

    # Define distinct line styles and colors
    line_styles = ['-', '--', '-.', ':']  # Solid, dashed, dash-dot, dotted
    colors = ['b', 'r', 'g', 'm']  # Blue, red, green, magenta

    # Create the plot
    plt.figure(figsize=(12, 7))

    for index, (values, best_fit) in enumerate(zip(values_set, best_fits)):
        plt.plot(weeks, values, marker='o', linestyle=line_styles[index], color=colors[index],
                 label=f"USR plot {index + 1}")
        plt.plot(year, best_fit, linestyle=line_styles[index], color=colors[index],
                 label=f"Best Fit {index + 1}")

    # Add labels and title
    plt.xlabel('Weeks')
    plt.ylabel('Inches')
    plt.title('USR Plot Data Predicted to 52 Weeks')
    plt.xticks(weeks)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Adjust the y-axis to reflect the range of the new data
    plt.ylim(0, 6)  # Adjust as necessary based on the data

    # Plotting the graph with best-fit lines
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    transect_usr_best_fit_data()

import matplotlib.pyplot as plt
import numpy as np

def transect_dsl_best_fit_data():
    # Defining the data for each pin at transect DSL
    weeks = np.array(list(range(1, 11)))  # 10 weeks (Week 1 to Week 10)

    values_set_1 = np.array([2, 2, 2.125, 2, 2, 2.0625, 2.0625, 2.25, 2.375, 2.3333])
    values_set_2 = np.array([2, 2.1875, 2.25, 2.875, 2.25, 2.25, 2.25, 2.25, 2.1875, 1.875])
    values_set_3 = np.array([2, 2.0625, 2.0625, 2, 2, 2.1875, 1.9375, 2, 2, 1.875])
    values_set_4 = np.array([2, 2.5, 2.5, 2.25, 2.5, 2.625, 2.0625, 2.75, 2, 2.25])
    values_set = np.array([values_set_1, values_set_2, values_set_3, values_set_4])

    # Computing best-fit lines for each dataset
    fits = [np.polyfit(weeks, values, 1) for values in values_set]

    # Data to extrapolate to 52 weeks
    year = np.linspace(1, 52)
    best_fits = [np.polyval(fit, year) for fit in fits]

    # Define distinct line styles and colors
    line_styles = ['-', '--', '-.', ':']  # Solid, dashed, dash-dot, dotted
    colors = ['b', 'r', 'g', 'm']  # Blue, red, green, magenta

    # Create the plot
    plt.figure(figsize=(12, 7))

    for index, (values, best_fit) in enumerate(zip(values_set, best_fits)):
        plt.plot(weeks, values, marker='o', linestyle=line_styles[index], color=colors[index],
                 label=f"DSL plot {index + 1}")
        plt.plot(year, best_fit, linestyle=line_styles[index], color=colors[index],
                 label=f"Best Fit {index + 1}")

    # Add labels and title
    plt.xlabel('Weeks')
    plt.ylabel('Inches')
    plt.title('DSL Plot Data Predicted to 52 Weeks')
    plt.xticks(weeks)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Adjust the y-axis to reflect the range of the new data
    plt.ylim(0, 6)  # Adjust as necessary based on the data

    # Plotting the graph with best-fit lines
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    transect_dsl_best_fit_data()

import matplotlib.pyplot as plt
import numpy as np

def transect_dsr_best_fit_data():
    # Defining the data for each pin at transect DSR
    weeks = np.array(list(range(1, 11)))  # 10 weeks (Week 1 to Week 10)

    values_set_1 = np.array([2, 2, 2.25, 2.5, 2, 2.25, 2, 2.375, 2.25, 2.375])
    values_set_2 = np.array([2, 2.5, 2.75, 1.75, 1.875, 1.9375, 1.75, 1.75, 2.5, 1.875])
    values_set_3 = np.array([2, 1.75, 2.0625, 1.5, 1.875, 1.5, 1.5625, 1.5, 1.625, 1.5])
    values_set_4 = np.array([2, 2, 1.75, 1.25, 1.5, 1.375, 1.5, 1.5, 1.5, 1.25])
    values_set_5 = np.array([2, 2, 2.125, 1.875, 1.75, 1.875, 2.5, 2, 2, 1.9375])
    values_set_6 = np.array([2, 2.0625, 2.625, 2.375, 2.375, 2.375, 2.9375, 1.875, 2.4375, 2.25])
    values_set_7 = np.array([2, 2.0625, 2.25, 2.125, 2.375, 1.5, 2.4375, 2, 2.5, 2.0625])
    values_set_8 = np.array([2, 2.25, 2.25, 2.375, 2.5, 2.375, 2.4375, 2.25, 2.75, 2.5])
    values_set = np.array([values_set_1, values_set_2, values_set_3, values_set_4,
                           values_set_5, values_set_6, values_set_7, values_set_8])

    # Computing best-fit lines for each dataset
    fits = [np.polyfit(weeks, values, 1) for values in values_set]

    # Data to extrapolate to 52 weeks
    year = np.linspace(1, 52)
    best_fits = [np.polyval(fit, year) for fit in fits]

    # Define distinct line styles and colors for all eight datasets
    line_styles = ['-', '--', '-.', ':', '-', '--', '-.', ':']  # Repeats styles for consistency
    colors = ['b', 'r', 'g', 'm', 'c', 'y', 'k', 'orange']  # Unique colors for each dataset

    # Create the plot
    plt.figure(figsize=(14, 8))  # Larger figure to accommodate more datasets

    for index, (values, best_fit) in enumerate(zip(values_set, best_fits)):
        plt.plot(weeks, values, marker='o', linestyle=line_styles[index], color=colors[index],
                 label=f"DSR plot {index + 1}")
        plt.plot(year, best_fit, linestyle=line_styles[index], color=colors[index],
                 label=f"Best Fit {index + 1}")

    # Add labels and title
    plt.xlabel('Weeks')
    plt.ylabel('Inches')
    plt.title('DSR Plot Data Predicted to 52 Weeks')
    plt.xticks(weeks)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Adjust the y-axis to reflect the range of the new data
    plt.ylim(0, 6)  # Adjust as necessary based on the data

    # Plotting the graph with best-fit lines
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    transect_dsr_best_fit_data()

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
