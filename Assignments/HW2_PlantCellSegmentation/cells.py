import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import skimage.io
from skimage.transform import resize
from skimage.color import rgb2gray
import time
from unionfind import *

def load_cells_grayscale(filename, n_pixels = 0):
    """
    Load in a grayscale image of the cells, where 1 is maximum brightness
    and 0 is minimum brightness

    Parameters
    ----------
    filename: string
        Path to image holding the cells
    n_pixels: int
        Number of pixels in the image
    
    Returns
    -------
    ndarray(N, N)
        A square grayscale image
    """
    cells_original = skimage.io.imread(filename)
    cells_gray = rgb2gray(cells_original)
    # Denoise a bit with a uniform filter
    cells_gray = ndimage.uniform_filter(cells_gray, size=10)
    cells_gray = cells_gray - np.min(cells_gray)
    cells_gray = cells_gray/np.max(cells_gray)
    N = int(np.sqrt(n_pixels))
    if n_pixels > 0:
        # Resize to a square image
        cells_gray = resize(cells_gray, (N, N), anti_aliasing=True)
    return cells_gray


def permute_labels(labels):
    """
    Shuffle around labels by raising them to a prime and
    modding by a large-ish prime, so that cells are easier
    to see against their backround
   
    Parameters
    ----------
    labels: ndarray(M, N)
        An array of labels for the pixels in the image
    Returns
    -------
    labels_shuffled: ndarray(M, N)
        A new image where the labels are different but still
        the same within connected components
    """
    return (labels**31) % 833

def get_cell_labels(arr, threshold):
    """
    Your method should return a 2D numpy array containing the labels of each cell; 
    that is, an image where each pixel that's in the same cell has the same number.

    To accomplish this, use your efficient union find implementation from lab 2 to merge 
    neighboring pixels together that are under the threshold. 
    Then, set the label of each pixel to be its root in union find.
    
    Parameters
    ----------
    arr: ndarray(N, N)
        An array of grayscale values, where 1 is maximum brightness
        and 0 is minimum brightness
    threshold: float
        Threshold for determining whether a pixel is a cell or not
    Returns
    -------
    labels: ndarray(N, N)
        An array of labels for the pixels in the image
    """
    rows, cols = arr.shape
    x = UnionFind(rows*cols) # Initialize union find
    for i in range(rows): # Iterate through rows of gray image
        for j in range(cols): # Iterate through columns of gray image
            if arr[i, j] > threshold: # If pixel is above threshold
                if i > 0 and arr[i-1, j] > threshold: # neighbor above is above threshold
                    x.union(i*cols+j, (i-1)*cols+j)
                if j > 0 and arr[i, j-1] > threshold: # neighbor to left is above threshold
                    x.union(i*cols+j, i*cols+j-1)
    labels = np.zeros((rows, cols)) # Initialize return array
    for i in range(rows):
        for j in range(cols):
            labels[i, j] = x.root(i*cols+j) # Set array pixel to root of pixel
    return labels

def get_cluster_centers(arr):
    """
    Returns a 2D numpy array containing the coordinates of the centers of each cell.

    Parameters
    ----------
    arr: ndarray(N, N)
        An array of labels for the pixels in the image
    Returns
    -------
    cluster_centers: ndarray(k, 2)
        an array of [i, j] locations of the centers of each cell
    """
    row, col = arr.shape
    cluster_centers = {}
    ret = []
    for i in range(row):
        for j in range(col):
            if arr[i, j] not in cluster_centers:
                cluster_centers[arr[i, j]] = []
                cluster_centers[arr[i, j]].append([i, j])
            else:
                cluster_centers[arr[i, j]].append([i, j])
    for key in cluster_centers.values():
        # average the x and y coordinates of the pixels in the each cluster
        if len(key) > 1:
            x = sum([x[0] for x in key])/len(key)
            y = sum([y[1] for y in key])/len(key)
            ret.append([x, y])
    return ret




if __name__ == '__main__':
    I = load_cells_grayscale("Cells.jpg")
    plt.imshow(I, cmap='magma')
    plt.show()
    thresh = 0.75
    I = load_cells_grayscale("Cells.jpg")
    labels = get_cell_labels(I, thresh)
    # permute_labels shuffles around the labels to make it 
    # easier to view the cells against their background
    plt.imshow(permute_labels(labels))
    plt.show()

    cells_original = skimage.io.imread("Cells.jpg")
    X = get_cluster_centers(labels)
    X = np.array(X)
    plt.imshow(cells_original)
    plt.scatter(X[:, 1], X[:, 0], c='C2')
    plt.show()

    