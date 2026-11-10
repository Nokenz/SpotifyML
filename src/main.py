import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.title("Ma première courbe")
plt.show() 