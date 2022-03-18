import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from stack import *

def delannoy(M, N):
    """
    Compute the Delannoy number D(M, N) using dynamic programming
    
    Parameters
    ----------
    M: int
        Number of samples in the first time series
    N: int
        Number of samples in the second time series
    
    Returns
    -------
    int: D(M, N)
    """
    D = np.ones((M, N), dtype=int)
    for i in range(1, M):
        for j in range(1, N):
            D[i, j] = D[i-1, j] + D[i, j-1] + D[i-1, j-1]
    return D[-1, -1]

def plot_all_warppaths(M, N, paths):
    """
    Make plots of all warping paths between two time series of
    specified lengths

    Parameters
    ----------
    M: int
        Number of samples in the first time series
    N: int
        Number of samples in the second time series
    path: list of list of [i, j]
        A list of constructed warping paths
    """
    frames = [] # for storing the generated images
    D = delannoy(M, N)
    fig = plt.figure(figsize=(M, N))
    for num, path in enumerate(paths):
        plot = []
        plot.append(plt.text(0.5, 1.01, "{} x {} Warping Path {} of {}".format(M, N, num+1, D),
                        horizontalalignment='center', verticalalignment='bottom',
                        transform=plt.gca().transAxes, size='large'))

        path = np.array(path)
        plot += plt.plot(path[:, 1], path[:, 0], c='C0')
        plot.append(plt.scatter(path[:, 1], path[:, 0], color='k', zorder=10))
        plt.xticks(np.arange(N), ["%i"%i for i in range(N)])
        plt.yticks(np.arange(M), ["%i"%i for i in range(M)])
        plt.gca().invert_yaxis()
        plt.ylabel("First Time Series")
        plt.xlabel("Second Time Series")
        frames.append(plot)
    ani = animation.ArtistAnimation(fig, frames, interval=250, blit=True, repeat_delay=1000)
    ani.save("paths.gif")

def get_warppath(M,N,path,all_paths):
    """
    Parameters
    ----------
    Return a list of all warping paths on an MxN grid

    M: int
        Number of samples in the first time series
    N: int
        Number of samples in the second time series
    path: list of [i, j]
        A list of warping paths
    all_paths: list of list of [i, j]
        A list of all warping paths
    
    """
    [i,j] = path[-1]
    if i == M-1 and j == N-1:
        all_paths.append(path.copy())
        #print(all_paths)
        return 
    if i+1 < M:
        path.append([i+1,j])
        get_warppath(M, N, path, all_paths)
        path.pop()
    if j+1 < N:
        path.append([i,j+1])
        get_warppath(M, N, path, all_paths)
        path.pop()
    if i+1 < M and j+1 < N:
        path.append([i+1,j+1])
        get_warppath(M, N, path, all_paths)
        path.pop()

def get_all_warppaths(M, N):
    """
    Parameters
    ----------
    Return a list of all warping paths on an MxN grid

    M: int
        Number of samples in the first time series
    N: int
        Number of samples in the second time series
    
    """
    ## TODO: Fill this in.  Call a recursive function to fill in paths with all possible warping paths
    path = [[0,0]]
    all_paths = []
    get_warppath(M, N, path, all_paths)
    #print(all_paths)
    return all_paths

if __name__ == '__main__':
    M = 3
    N = 5
    paths = get_all_warppaths(M, N)
    plot_all_warppaths(M, N, paths)