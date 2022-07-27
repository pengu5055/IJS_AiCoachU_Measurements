import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
import pandas as pd

colors = cmr.take_cmap_colors("cmr.torch", 20, cmap_range=(0.2, 0.8), return_fmt="hex")

# Import tables
# alpha = pd.read_table("alpha.csv", sep=",", header=2, dtype={'AccX [mg]':'int16'}).to_numpy()
alpha = np.genfromtxt("alpha.csv", delimiter=",", skip_header=2, invalid_raise=False)

time = alpha[:, 2]
acc_x = alpha[:, 3]

plt.plot(time, acc_x, color=colors[5], lw=2)
plt.show()
