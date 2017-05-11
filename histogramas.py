import numpy as np
import matplotlib.pyplot as plt


datos = [[1838, 1442, 562, 560, 324, 126, 67, 48, 19, 18], [341, 324, 311, 304, 291, 274, 259, 247, 244, 237]] 
impr = ["Peliculas", "votos"]
X = np.arange(10)
plt.bar(X + 0.00, datos[0], color = "b", width = 0.25)
plt.bar(X + 0.25, datos[1], color = "r", width = 0.25)
plt.xticks(X+0.38, ["0.5","1","1.5","2", "2.5", "3", "3.5", "4", "4.5", "5" ])
plt.show()


