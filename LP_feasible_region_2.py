# E22 p508 chap 9 Linear Programming - Introduction to management science (B. Taylor)
# A fruit grower has 150 acres of land available to raise two crops, A and B.
# It takes one day to trim an acre of crop A and two days to trim an acre of crop B,
# and there are 240 days per year available for trimming. It takes 0.3 day to pick an acre
# of crop A and 0.1 day to pick an acre of crop B, and there are 30 days per year available
# for picking. Find the number of acres of each fruit that should be planted to maximize profit,
# assuming that the profit is $140 per acre for crop A and $235 per acre for B.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def eq_1(x, y):
    return x + y - 150


def eq_2(x, y):
    return x + 2 * y - 240


def eq_3(x, y):
    return 3 * x + y - 300


def objective_function(x, y):
    return 70 * x + 47 * y


def lattice():
    # decision variables are integers
    lattice_points = []
    corners = []
    for i in range(max_x + 1):
        for j in range(max_y + 1):

            if eq_1(i, j) <= 0 and eq_2(i, j) <= 0 and eq_3(i, j) <= 0:
                lattice_points.append([i, j])

                if i == 0 and (j == 0 or eq_1(i, j) == 0 or eq_2(i, j) == 0 or eq_3(i, j) == 0):
                    corners.append([i, j])
                elif j == 0 and (eq_1(i, j) == 0 or eq_2(i, j) == 0 or eq_3(i, j) == 0):
                    corners.append([i, j])
                elif eq_1(i, j) == 0 and (eq_2(i, j) == 0 or eq_3(i, j) == 0):
                    corners.append([i, j])
                elif eq_2(i, j) == 0 and eq_3(i, j) == 0:
                    corners.append([i, j])
    return lattice_points, corners


def lattice_point_testing(vertex_list):

    """
    max_z = 0
    star_x, star_y = 0, 0
    for i in range(len(vertex_list)):
        x_i = vertex_list[i][0]
        y_i = vertex_list[i][1]
        z_value = objective_function(x_i, y_i)
        if z_value > max_z:
            max_z = z_value
            star_x = x_i
            star_y = y_i
    return star_x, star_y, max_z
    """
    optimal_vertex = max(vertex_list,
                         key=lambda vertex: objective_function(vertex[0], vertex[1]))
    return *optimal_vertex, objective_function(*optimal_vertex)


def feasible_region(x, y1, y2, y3, graphs_labels, int_points, vertices, optimal_solution):
    # plot constraints
    plt.plot(x, y1, label=fr'${graphs_labels[0]}$')
    plt.plot(x, y2, label=fr'${graphs_labels[1]}$')
    plt.plot(x, y3, label=fr'${graphs_labels[2]}$')
    # corners
    x_corner, y_corner = zip(* vertices)
    plt.scatter(x_corner, y_corner,
                c="gray", marker="o", edgecolor="red", s=50,
                label=f'{vertices}')
    # lattice points
    x_lattice, y_lattice = zip(*int_points)
    plt.scatter(x_lattice, y_lattice, c="blue", marker="o", edgecolor="red", s=20)
    # feasible region
    plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3),
                     color='pink', alpha=0.8)
    # optimal_solution
    plt.scatter(optimal_solution[0], optimal_solution[1],
                marker="*", s=130, label=f'Optimal solution {optimal_solution}')


def objective_line(x, c, k):
    # objective function c[0] * x + c[1] * y = k
    plt.plot(x, (k - c[0] * x) / c[1],
             'k', label='Objective function')
    length_c = np.sqrt(c[0] ** 2 + c[1] ** 2)
    plt.arrow(k / (c[0] * 2), k // (c[1] * 2), 5 * c[0] / length_c, 5 * c[1] / length_c,
              head_width=2.5, head_length=5,
              color='green', linestyle='--')


def plot_options(x_max, y_max, x_label, y_label, major_dist, minor_dist):
    plt.xlim(-0.2, x_max)
    plt.ylim(-0.2, y_max)
    plt.xlabel(f'{x_label}')
    plt.ylabel(f'{y_label}')

    plt.title('Feasible Region')
    plt.legend(loc='upper right')
    plt.grid(True)
    # major tick marks
    plt.xticks(np.arange(0, x_max, major_dist))
    plt.yticks(np.arange(0, y_max, major_dist))
    plt.gca().set_aspect('equal', adjustable='box')

    # Set minor ticks and grid
    ax = plt.gca()
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(minor_dist))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(minor_dist))
    ax.grid(which='minor', linestyle=':', linewidth=0.5)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plt.rcParams['text.usetex'] = True

    # global variable
    max_x, max_y = 150, 150
    x1 = np.linspace(0, max_x, 1000)
    graph_labels = ['x + y = 150', 'x  + 2y = 240', '3x + y = 150']
    f1, f2, f3 = 150 - x1, 120 - x1 / 2, 300 - 3 * x1

    integer_points, vertices_ = lattice()
    optimal_ = lattice_point_testing(integer_points)

    feasible_region(x1, f1, f2, f3, ['x + y = 150', 'x + 2y = 240', '3x + y = 300'],
                    integer_points, vertices_, optimal_)

    objective_line(x1, [70, 47], 70 * 47)
    plot_options(max_x, max_y, 'crop A', 'crop B', 10, 5)
