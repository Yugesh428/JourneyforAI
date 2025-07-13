import numpy as np

# Step 1: Make a matrix A
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Step 2: QR decomposition
Q, R = np.linalg.qr(A)

# Step 3: Print results
print("Matrix A:")
print(A)

print("\nMatrix Q:")
print(Q)

print("\nMatrix R:")
print(R)
