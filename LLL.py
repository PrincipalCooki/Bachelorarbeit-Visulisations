import numpy as np
import matplotlib.pyplot as plt

# Function to perform Gram-Schmidt orthogonalization
def gram_schmidt(basis):
    B = np.array(basis, dtype=float)
    n = B.shape[0]
    U = np.zeros_like(B)
    U[0] = B[0]
    for i in range(1, n):
        proj = np.sum([(np.dot(B[i], U[j]) / np.dot(U[j], U[j])) * U[j] for j in range(i)], axis=0)
        U[i] = B[i] - proj
    return U

# Function to perform one step of the LLL algorithm
def lll_step(basis):
    B = np.array(basis, dtype=float)
    n = B.shape[0]
    U = gram_schmidt(B)
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            mu = np.dot(B[k], U[j]) / np.dot(U[j], U[j])
            if abs(mu) > 0.5:
                B[k] = B[k] - np.round(mu) * B[j]
                U = gram_schmidt(B)
        if np.dot(U[k], U[k]) >= (0.75 - (np.dot(U[k - 1], B[k]) / np.dot(U[k - 1], U[k - 1])) ** 2) * np.dot(U[k - 1], U[k - 1]):
            k += 1
        else:
            B[[k, k - 1]] = B[[k - 1, k]]
            U = gram_schmidt(B)
            k = max(k - 1, 1)
    return B

# Initial lattice basis
basis = np.array([[4, 1], [2, 3]])

# Perform one step of the LLL algorithm
reduced_basis = lll_step(basis)

# Visualization
plt.figure(figsize=(8, 8))
origin = np.array([0, 0])

# Plot original basis
plt.quiver(*origin, *basis[0], color='r', scale=1, scale_units='xy', angles='xy')
plt.quiver(*origin, *basis[1], color='r', scale=1, scale_units='xy', angles='xy')

# Plot reduced basis
plt.quiver(*origin, *reduced_basis[0], color='b', scale=1, scale_units='xy', angles='xy')
plt.quiver(*origin, *reduced_basis[1], color='b', scale=1, scale_units='xy', angles='xy')

# Create custom legends
plt.plot([], [], 'r', label='Original Basis')
plt.plot([], [], 'b', label='Reduced Basis')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid(True)
plt.legend()
plt.title('One Step of the LLL Algorithm')
plt.show()
