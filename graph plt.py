import numpy as np
import matplotlib.pyplot as plt
d1=np.array([1, 2, 3, 4, 5])
d2=np.array([1, 3, 4, 5, 10])
plt.plot(d1,d2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample Plot")
plt.grid(True)
plt.show()