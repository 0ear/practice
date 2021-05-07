import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,50)
y = 2*x+3
y1 = 30*x+3
y2 = 90*x+3
plt.plot(x, y, c ='r')
plt.plot(x, y1, c = 'g')
plt.plot(x, y2, c = 'b')
plt.show()