import numpy as np
import matplotlib.pyplot as plt

# Create a 5x5 matrix using diagflat and ones functions
matrix = np.diagflat(np.ones(5))
eigenvalues, eigenvectors = np.linalg.eig(matrix)
fifth_eigenvector = eigenvectors[:, 4]
x_values = np.linspace(0, 1, 5)

# Define the function sqrt(2) * sin(pi * x)
function_values = np.sqrt(2) * np.sin(np.pi * x_values)

plt.plot(x_values, fifth_eigenvector, label='Fifth Eigenvector')

# Plot the function sqrt(2) * sin(pi * x) for comparison
plt.plot(x_values, function_values, label='sqrt(2) * sin(pi * x)')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()

# Just turning the plot into an actual image
plt.savefig('fifth_eigenvector_plot.png')
plt.show()

