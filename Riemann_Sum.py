
import numpy as np
import matplotlib.pyplot as plt


def f(x1):
    return 1 / (1 + x1 ** 2)


def plot_f(smooth_scale_1):
    # use smooth_scale * num_intervals + 1 points  to plot the function smoothly
    x2 = np.linspace(x_min, x_max, smooth_scale_1 * num_intervals + 1)
    plt.plot(x2, f(x2), 'b')


def sample_points(method_str):
    sample_dict = {
        'left': (x[:-1], f(x[:-1]), 1, 'edge', step),
        'midpoint': ((x[:-1] + x[1:]) / 2, f((x[:-1] + x[1:]) / 2), 2, 'center', step),
        'right': (x[1:], f(x[1:]), 3, 'edge', -step)
    }

    return sample_dict[method_str]


def plot_riemann_sum(method_str):
    x_, y_, subplot_index_, align_, width_ = sample_points(method_str)

    plt.subplot(1, 3, subplot_index_)
    # plot function f
    plot_f(smooth_scale)
    # plot points (x_i * , f(x_i*))
    plt.plot(x_, y_,
             'b.', markersize=10)
    # plot rectangles
    plt.bar(x_, y_,
            width=width_, alpha=0.2,
            align=align_, edgecolor='b',
            animated=True)
    plt.title(f'{method_str} Riemann Sum using {num_intervals} sub-intervals')
    plt.xlabel('x')
    plt.ylabel('f(x)')


def riemann_sum(method_str):
    x_, y_, subplot_index_, align_, width_ = sample_points(method_str)
    return round(step * np.sum(f(x_)), 5)


if __name__ == '__main__':
    # parameters
    x_min = 0
    x_max = 5
    num_intervals = 10
    smooth_scale = 10  # to plot function more smoothly

    # Compute the definite integral using Riemann sum
    step = (x_max - x_min) / num_intervals
    x = np.linspace(x_min, x_max, num_intervals + 1)

    plt.figure(figsize=(15, 5))
    plot_riemann_sum('left')
    plot_riemann_sum('midpoint')
    plot_riemann_sum('right')

    plt.tight_layout()
    plt.show()
    # Results:
    print(f"Left Riemann Sum     : {riemann_sum('left')} using {num_intervals} sub-intervals")
    print(f"Midpoint Riemann Sum : {riemann_sum('midpoint')} using {num_intervals} sub-intervals")
    print(f"Right Riemann Sum    : {riemann_sum('right')} using {num_intervals} sub-intervals")
