import matplotlib.pyplot as plt
import numpy as np

# Parameters
lattice_size = 100  # Increased to cover a larger area
noise_level = 0.3
range_limit = 5  # Limit for the square [-5, 5]

# Define a new basis (transformation matrix)
transformation_matrix = np.array([[3, 1], [4, 1]])

# Create lattice points
x = np.arange(-lattice_size, lattice_size + 1)
y = np.arange(-lattice_size, lattice_size + 1)
x, y = np.meshgrid(x, y)

# Flatten the points to apply the transformation
points = np.vstack([x.ravel(), y.ravel()])
transformed_points = transformation_matrix @ points

# Reshape back to grid
x_transformed = transformed_points[0].reshape(x.shape)
y_transformed = transformed_points[1].reshape(y.shape)

# Add noise
x_noise = x_transformed + noise_level * np.random.randn(*x_transformed.shape)
y_noise = y_transformed + noise_level * np.random.randn(*y_transformed.shape)

# Filter points within the range [-5, 5]
mask = (x_transformed >= -range_limit) & (x_transformed <= range_limit) & \
       (y_transformed >= -range_limit) & (y_transformed <= range_limit)

# Plotting the lattice with noise
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Noisy points only
axs[0].scatter(x_noise[mask], y_noise[mask], c='blue', marker='o', label='Noisy Points')
axs[0].set_title("Noisy Points Only")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Y")
axs[0].grid(True)
axs[0].set_xlim(-range_limit, range_limit)
axs[0].set_ylim(-range_limit, range_limit)

# Original lattice with noise
axs[1].scatter(x_transformed[mask], y_transformed[mask], c='red', marker='o', label='Transformed Points')
axs[1].scatter(x_noise[mask], y_noise[mask], c='blue', marker='o', label='Noisy Points')

# Connect original points to noisy points with lines
for i in range(x_transformed.shape[0]):
    for j in range(x_transformed.shape[1]):
        if mask[i, j]:
            axs[1].plot([x_transformed[i, j], x_noise[i, j]],
                        [y_transformed[i, j], y_noise[i, j]], 'k--', linewidth=0.5)

axs[1].set_title("Transformed Lattice with Noise")
axs[1].set_xlabel("X")
axs[1].set_ylabel("Y")
axs[1].legend()
axs[1].grid(True)
axs[1].set_xlim(-range_limit, range_limit)
axs[1].set_ylim(-range_limit, range_limit)

plt.tight_layout()
plt.show()