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



b_1 = np.array([32, 24])
b_2 = np.array([37, 42])
basis1 = np.array([b_1, b_2])  # standard basis
basis2 = np.array([-b_2 + b_1, 3*b_1 - 2 * b_2])  # Different basis

target_vector = np.array([-60,48])
closest_lattice_point = np.array([-61, 54])

range_vals = np.arange(-150, 150)
lattice_points1 = generate_lattice_points(basis1, range_vals)
lattice_points2 = generate_lattice_points(basis2, range_vals)





plt.scatter(lattice_points1[:, 0], lattice_points1[:, 1], color='black', s=10)
plt.quiver(0, 0, *basis1[0], color='r', scale=1, scale_units='xy', angles='xy', width=0.004)
plt.quiver(0, 0, *basis1[1], color='r', scale=1, scale_units='xy', angles='xy', width=0.004)
plt.plot(target_vector[0], target_vector[1], 'bo', label='Target Vector')

plt.plot(closest_lattice_point[0], closest_lattice_point[1], 'go', label='Closest Lattice Point')

line_xs = [target_vector[0], closest_lattice_point[0]]
line_ys = [target_vector[1], closest_lattice_point[1]]
plt.plot(line_xs, line_ys, 'b')

mid_x = (target_vector[0] + closest_lattice_point[0]) / 2
mid_y = (target_vector[1] + closest_lattice_point[1]) / 2
plt.text(mid_x, mid_y, '< d', fontsize=12, ha='center', va='bottom')

plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
