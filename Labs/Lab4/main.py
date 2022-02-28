import numpy as np
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
    D = np.zeros((M,N))
    D[0,0] = distance(X[0],Y[0])
    S = [] # backtracing array
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
                S.append((i,j))
    #return D[M-1,N-1]
    return S

X = np.array([[0, 2], [17, 0], [25, 0], [31, 0]])
Y = np.array([[0, 4], [5, 4], [16, 4], [24, 4], [30, 4]])
print(dtw(X, Y))