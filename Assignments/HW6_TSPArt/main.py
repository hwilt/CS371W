import numpy as np
import matplotlib.pyplot as plt
import skimage.io
from stipple import *


'''I = skimage.io.imread("images/layla.png")
X = voronoi_stipple(I, thresh=0.4, target_points=10000, canny_sigma=3, n_iters=10)
plt.figure(figsize=(10, 10))
plt.scatter(X[:, 0], X[:, 1], 2)
plt.show()'''

np.random.seed(0)
I = skimage.io.imread("images/penguins.png")
# Initial stippling
X = voronoi_stipple(I, thresh=0.3, target_points=2000, canny_sigma=0.8)
# Filter out lowest 4 points by density
X = density_filter(X, (X.shape[0]-4)/X.shape[0]) 
plt.figure(figsize=(10, 10))
plt.scatter(X[:, 0], X[:, 1], 2)
plt.savefig("penguins_stipple.svg", bbox_inches='tight')
plt.show()