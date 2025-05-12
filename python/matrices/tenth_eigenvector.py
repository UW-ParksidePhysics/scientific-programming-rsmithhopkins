import numpy as np
import matplotlib.pyplot as plt

# Set the matrix dimension
matrix_dimension = 10

matrix = np.diagflat(np.ones(matrix_dimension))
eigenvalues, eigenvectors = np.linalg.eig(matrix)
tenth_eigenvector = eigenvectors[:, 9]
x_values = np.linspace(0, 1, matrix_dimension)

# Define the function sqrt(2) * sin(pi * x)
function_values = np.sqrt(2) * np.sin(np.pi * x_values)

plt.plot(x_values, tenth_eigenvector, label='Tenth Eigenvector')

# Plot the function sqrt(2) * sin(pi * x) for comparison
plt.plot(x_values, function_values, label='sqrt(2) * sin(pi * x)')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()

# Just turning the plot into an actual image
plt.savefig('tenth_eigenvector_plot.png')
plt.show()