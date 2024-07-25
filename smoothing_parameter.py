import numpy as np
import matplotlib.pyplot as plt


def gaussian_noise(mu, sigma, size):
    return np.random.normal(mu, sigma, size)


basis_vector_1 = np.array([1, 0.5])
basis_vector_2 = np.array([0.5, 1])

num_samples = 10000

mu = 0
width = 0.2  # Smoothing parameter
noise_vectors = gaussian_noise(mu, width, (num_samples, 2))

modulo_vectors = np.zeros_like(noise_vectors)
inv_basis_matrix = np.linalg.inv(np.array([basis_vector_1, basis_vector_2]).T)
for i, vec in enumerate(noise_vectors):
    coeffs = inv_basis_matrix @ vec
    coeffs_mod = np.mod(coeffs, 1)
    modulo_vectors[i] = (coeffs_mod[0] * basis_vector_1) + (coeffs_mod[1] * basis_vector_2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(noise_vectors[:, 0], noise_vectors[:, 1], alpha=0.5, s=1)
plt.title('Original Gaussian Noise Vectors')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(modulo_vectors[:, 0], modulo_vectors[:, 1], alpha=0.5, s=1)
plt.title('Reduced Vectors Modulo Fundamental Parallelepiped')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.tight_layout()
plt.show()
