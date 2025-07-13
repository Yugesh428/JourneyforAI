import numpy as np
from scipy.linalg import lu

A = np.array([[4, 3],
              [6, 3]])

P, L, U = lu(A)

print("P (Permutation matrix):\n", P)
print("L (Lower triangular):\n", L)
print("U (Upper triangular):\n", U)
