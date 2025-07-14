import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[0, 1],
              [1, 0]])

x = np.array([1, 1])

# Apply T1 then T2
result = B @ (A @ x)
print("Result of T2(T1(x)):", result)

# Alternatively using composed matrix
composed_matrix = B @ A
result2 = composed_matrix @ x
print("Using composed matrix:", result2)
