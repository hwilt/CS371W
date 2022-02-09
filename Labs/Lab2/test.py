import numpy as np
import matplotlib.pyplot as plt
from unionfind import *
from unionfindopt import *
from djsetslow import *

if __name__ == '__main__':
    Ns = np.arange(10, 400, 10)
    ops_djsetslow = np.zeros(Ns.size)
    ops_unionfind = np.zeros(Ns.size)
    ops_unionfind_opt = np.zeros(Ns.size)
    np.random.seed(0)

    for i, N in enumerate(Ns):
        print(N, end=' ', flush=True)
        s = SlowDisjointSet(N)
        u = UnionFind(N)
        uo = UnionFindOpt(N)
        # Choose a bunch of random pairs of indices and union them
        for k in range(N):
            i1 = np.random.randint(N)
            i2 = np.random.randint(N)
            s.union(i1, i2)
            u.union(i1, i2)
            uo.union(i1, i2)
        # Check to make sure the data structures agree
        for i1 in range(N):
            for i2 in range(i1+1, N):
                assert(s.find(i1, i2) == u.find(i1, i2))
                assert(u.find(i1, i2) == uo.find(i1, i2))
        # Record the number of operations
        ops_djsetslow[i] += s._operations / s._calls
        ops_unionfind[i] += u._operations / u._calls
        ops_unionfind_opt[i] += uo._operations / uo._calls
    
    plt.figure(figsize=(12, 4))
    plt.plot(Ns, ops_djsetslow)
    plt.plot(Ns, ops_unionfind)
    plt.plot(Ns, ops_unionfind_opt)
    plt.legend(["Slow", "Union Find", "Union Find Optimal"])
    plt.xlabel("N")
    plt.ylabel("Amortized Operations")
    #plt.yscale("log")
    plt.show()
