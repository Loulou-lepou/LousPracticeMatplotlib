# Hyperbolic functions  https://en.wikipedia.org/wiki/Hyperbolic_functions
# My Maple code:

import numpy as np
import matplotlib.pyplot as plt


# render tex in title, legend, tick marks
plt.rcParams['text.usetex'] = True

lim = 8
size = 5.6
fig, ax = plt.subplots(figsize=(size, size))
# unpack tuple (fig, ax) into variables fig & ax
# plt.subplots() -> tuple (fig, ax) containing a figure (fig), & axes objects (objs that have plotting methods)

xs = np.linspace(-lim, lim, 1000)
# plot y = sinh(x)
ax.plot(xs, np.sinh(xs),
        label=r"$ y = sinh(x) $",
        color="#b30000",
        linestyle="-",
        linewidth=2)

# plot y = cosh(x)
ax.plot(xs, np.cosh(xs),
        label=r"$ y = cosh(x)$",
        color="#00b300",
        linestyle="--",
        linewidth=2)

# plot y = tanh(x)
ax.plot(xs, np.tanh(xs),
        label=r"$ y = tanh(x)$",
        color="#0000b3",
        linestyle=":",
        linewidth=2)

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_xticks([-1, 0, 1])
ax.set_yticks([-1, 0, 1])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid("on")
ax.legend(loc="lower right")
fig.tight_layout()
fig.savefig("sinh_cosh_tanh.svg", transparent=True)
