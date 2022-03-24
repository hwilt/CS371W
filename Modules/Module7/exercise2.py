import numpy as np

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def shuffle(arr):
    N = len(arr)
    for i in range(N-1):
        # TODO: Pick a random index between
        # 0 and N-i-1, inclusive, and swap this 
        # index with index N-i-1
        swap(arr, np.random.randint(0, N-i), N-i-1)


np.random.seed(0)
arr = np.arange(10)
print(arr)
shuffle(arr)
arr = "{}".format(arr)
print(arr)