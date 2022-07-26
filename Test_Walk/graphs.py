import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
import pandas as pd

# Import tables
alpha = pd.read_table("alpha.csv", sep=",", header=2).to_numpy()

# Use boolean mask
mask = (alpha[:, 0] == "D")
a_data = alpha[mask, :]


time = alpha[:, 3].astype("float32")
print(time)
plt.plot(time, alpha[:, 4])
plt.show()
