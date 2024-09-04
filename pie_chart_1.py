# import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


# when use on mac:
# mpl.use('macosx')

# 1. line graph
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
y2 = y + 0.5
# Avoid ValueError: x & y don't have the same first dimension
plt.plot(x, y, label="graph 1")
plt.plot(x, y2, label="graph 2")
plt.title("My title")
plt.legend(loc='best')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

# 2. pie chart
# src: https://matplotlib.org/stable/gallery/pie_and_polar_charts/
# pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["375 g flour", "75 g sugar", "250 g butter", "300 g berries"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"


wedges, texts, autotexts = \
    ax.pie(data,
           autopct=lambda pct: func(pct, data),
           textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Show grid
ax.grid(True)

# Show axes
ax.axhline(0, color='black', linewidth=0.5, ls='--')
ax.axvline(0, color='black', linewidth=0.5, ls='--')

# Set tick marks with spacing of 0.2
ax.set_xticks(np.arange(-1, 1.1, 0.2))
ax.set_yticks(np.arange(-1, 1.1, 0.2))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Matplotlib bakery: A pie")

plt.show()
