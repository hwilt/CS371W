def A(m, n, counts, memory = {}, do_print = True):
    res = 0
    counts[0] += 1
    if (m, n) in memory:
        return memory[(m, n)]
    if m == 0:
        res = n+1
    elif n == 0:
        if (m-1, 1) in memory:
            res = memory[(m-1, 1)]
        else:
            res = A(m-1, 1, counts, memory)
            memory[m-1, 1] = res
    else:
        ## TODO: Add memoization here for A(m, n-1)
        inner = 0
        if (m, n-1) in memory:
            inner = memory[(m, n-1)]
        else:
            inner = A(m, n-1, counts, memory)
            memory[m, n-1] = inner
        ## TODO: Add memoization here for A(m-1, inner)
        if (m-1, inner) in memory:
            res += memory[(m-1, inner)]
        else:
            res += A(m-1, inner, counts, memory)
            memory[m-1, inner] = res
        #res = A(m-1, inner, counts, memory)
    return res

counts = [0]
print(A(2, 3, counts, {}), end=".")
print(counts[0], end="_")
counts = [0]
print(A(3, 3, counts, {}), end=".")
print(counts[0], end="_")
counts = [0]
print(A(4, 0, counts, {}), end=".")
print(counts[0])