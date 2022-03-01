import numpy as np
import matplotlib.pyplot as plt

def distance(u, v):
    """
    Compute the Euclidean distance between two points
    in d dimensions
     
    Parameters
    ----------
    u: ndarray(d)
        First point
    v: ndarray(d)
        Second point
     
    Return
    ------
    float: The distance between the two points
    """
    u = np.array(u)
    v = np.array(v)
    return np.sqrt(np.sum((u-v)**2))

def dtw(X,Y):
    """
    Dynamic Time Warping
    """
    M = len(X)
    N = len(Y)
    # Make 2D array that stores the optimal moves
    moves = []
    for i in range(M):
        moves.append([])
        for j in range(N):
            moves[i].append([])
    D = np.zeros((M,N))
    D[0,0] = distance(X[0],Y[0])
    for i in range(0,M):
        for j in range(0,N):
            if j == 0 and i != 0:
                D[i,j] = D[i-1,j] + distance(X[i],Y[j])
            elif i == 0 and j != 0:
                D[i,j] = D[i,j-1] + distance(X[i],Y[j])
            else:
                cost1 = D[i-1,j] + distance(X[i],Y[j])
                cost2 = D[i,j-1] + distance(X[i],Y[j])
                cost3 = D[i-1,j-1] + distance(X[i],Y[j])
                D[i,j] = min(cost1,cost2,cost3)
                moves[i][j] = np.argmin([cost1,cost2,cost3]) + 1
                
    i = M - 1 
    j = N - 1
    path = [] # backtracing array
    while i >= 0 and j >= 0:
        if moves[i][j] == 1:
            path.append([i,j])
            i -= 1
        elif moves[i][j] == 2:
            path.append([i,j])
            j -= 1
        else:
            path.append([i,j])
            i -= 1
            j -= 1
    path.append([0,0])
    path.reverse()
    #return D[M-1,N-1]
    return path


def main():

    # Example 1: Traile vs Bolt
    '''X = np.array([[0, 2], [17, 0], [25, 0], [31, 0]])
    Y = np.array([[0, 4], [5, 4], [16, 4], [24, 4], [30, 4]])
    print(dtw(X, Y))'''

    # Example 2: Figure 8s
    N = 50
    t = np.linspace(0, 1, N)
    X = np.zeros((N, 2))
    X[:, 0] = np.cos(2*np.pi*t)
    X[:, 1] = np.sin(4*np.pi*t)
    Y = np.zeros((N, 2))
    Y[:, 0] = 1.3*np.cos(2*np.pi*(t**2))
    Y[:, 1] = 1.3*np.sin(4*np.pi*(t**2))+0.1
    path = np.array(dtw(X, Y))
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.plot(X[:, 0], X[:, 1], c='C0')
    plt.scatter(X[:, 0], X[:, 1], c='C0')
    plt.plot(Y[:, 0], Y[:, 1], c='C1')
    plt.scatter(Y[:, 0], Y[:, 1], c='C1')
    path = np.array(path)
    for [i, j] in path:
        plt.plot([X[i, 0], Y[j, 0]], [X[i, 1], Y[j, 1]], color='k')
    plt.subplot(122)
    plt.plot(path[:, 1], path[:, 0])
    plt.title("Warping Path")
    plt.ylabel("Blue Curve")
    plt.xlabel("Orange Curve")
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    main()