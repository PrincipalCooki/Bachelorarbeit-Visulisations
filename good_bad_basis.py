import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def generate_lattice_points(basis, range_vals):
    points = []
    for i in range_vals:
        for j in range_vals:
            point = i * basis[0] + j * basis[1]
            points.append(point)
    return np.array(points)


def add_parallelepiped(ax, basis):
    points = np.array([[0, 0], basis[0], basis[0] + basis[1], basis[1]])
    polygon = Polygon(points, closed=True, color='blue', alpha=0.3)
    ax.add_patch(polygon)


b_1 = np.array([3.2, 2.4])
b_2 = np.array([3.7, 4.2])
basis1 = np.array([b_1, b_2])  # standard basis
basis2 = np.array([-b_2 + b_1, 3*b_1 - 2 * b_2])  # Different basis

range_vals = np.arange(-100, 100)
lattice_points1 = generate_lattice_points(basis1, range_vals)
lattice_points2 = generate_lattice_points(basis2, range_vals)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.scatter(lattice_points1[:, 0], lattice_points1[:, 1], color='black', s=10)
ax1.quiver(0, 0, *basis1[0], color='r', scale=1, scale_units='xy', angles='xy', width=0.004)
ax1.quiver(0, 0, *basis1[1], color='r', scale=1, scale_units='xy', angles='xy', width=0.004)
add_parallelepiped(ax1, basis1)
ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax1.axhline(0, color='black', lw=1)
ax1.axvline(0, color='black', lw=1)
ax1.grid(True)

ax2.scatter(lattice_points2[:, 0], lattice_points2[:, 1], color='black', s=10)
ax2.quiver(0, 0, *basis2[0], color='g', scale=1, scale_units='xy', angles='xy', width=0.004)
ax2.quiver(0, 0, *basis2[1], color='g', scale=1, scale_units='xy', angles='xy', width=0.004)
add_parallelepiped(ax2, basis2)
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.axhline(0, color='black', lw=1)
ax2.axvline(0, color='black', lw=1)
ax2.grid(True)

plt.show()
