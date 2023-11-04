import numpy as np
import matplotlib.pyplot as plt

# sin^2(x) + cos^2(x) = 1 identity
x1 = np.arange(-100, 100, 0.1)
y1 = (np.sin(np.radians(x1)) ** 2) +  (np.cos(np.radians(x1)) ** 2)

# sine wave graph
x2 = np.arange(-100, 100, 0.1)
y2 = np.sin(np.radians(x2)*10)


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()