import numpy as np


matrix_three = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, -2]])
print(f'A_3 = {matrix_three}\n')

size = 2
identity_three = np.identity(size)
negative_ones = np.full(size-1, -1)
down_shifted_negative_ones = np.diag(negative_ones, -1)
up_shifted_negative_ones = np.diag(negative_ones, 1)
combined_matrix = 2*identity_three + down_shifted_negative_ones + up_shifted_negative_ones
print(f'\n{combined_matrix}\n')

eigenvalues, eigenvectors = np.linalg.eigh(combined_matrix)

for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors.transpose()):
    print(f'lambda = {eigenvalue}, x-vector = {eigenvector}\n')
