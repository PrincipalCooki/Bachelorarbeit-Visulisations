import numpy as np
import matplotlib.pyplot as plt

# Define a function to generate lattice points
def generate_lattice_points(basis, range_vals):
    points = []
    for i in range_vals:
        for j in range_vals:
            point = i * basis[0] + j * basis[1]
            points.append(point)
    return np.array(points)

# Define the original basis and a different basis
basis1 = np.array([[3.6, 2.6], [5, 3.8]])  # standard basis
basis2 = np.array([[0.8, 0.2], [0.2, -0.8]])  # Different basis

# Generate lattice points
range_vals = np.arange(-5, 6)
lattice_points1 = generate_lattice_points(basis1, range_vals)
lattice_points2 = generate_lattice_points(basis2, range_vals)

# Plot lattice points
plt.figure(figsize=(8, 8))
plt.scatter(lattice_points1[:, 0], lattice_points1[:, 1], color='black', s=10)

# Plot basis vectors
origin = np.array([0, 0])
plt.quiver(*origin, *basis1[0], color='r', scale=1, scale_units='xy', angles='xy', width=0.001)
plt.quiver(*origin, *basis1[1], color='r', scale=1, scale_units='xy', angles='xy', width=0.001)
plt.quiver(*origin, *basis2[0], color='g', scale=1, scale_units='xy', angles='xy', width=0.001)
plt.quiver(*origin, *basis2[1], color='g', scale=1, scale_units='xy', angles='xy', width=0.001)

# Customize plot
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.grid(True)
plt.title('Lattice Points with Different Bases')
plt.show()
