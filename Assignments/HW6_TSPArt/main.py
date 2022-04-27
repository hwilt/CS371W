import numpy as np
import matplotlib.pyplot as plt
import skimage.io
from stipple import *
I = skimage.io.imread("images/layla.png")
X = voronoi_stipple(I, thresh=0.4, target_points=10000, canny_sigma=3, n_iters=10)
plt.figure(figsize=(10, 10))
plt.scatter(X[:, 0], X[:, 1], 2)
plt.show()