def swap(arr, i, j):
    """
    Use this as a helper method to swap two elements in an array
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def merge(x, y, i1, mid, i2):
    """
    Perform a merge of two contiguous sorted sub-chunks of
    the array x, using y as a staging area

    Parameters
    ----------
    x: list
        The main array
    y: list
        The array to copy into as the two chunks are being merged
    i1: int
        Left of first chunk
    mid: int
        Right of first chunk
    i2: int
        End of second chunk
    """
    i = i1
    j = mid+1
    k = i1
    while i <= mid and j <= i2:
        if x[i] < x[j]:
            y[k] = x[i]
            i += 1
        else:
            y[k] = x[j]
            j += 1
        k += 1
    while i <= mid:
        y[k] = x[i]
        i += 1
        k += 1
    while j <= i2:
        y[k] = x[j]
        j += 1
        k += 1
    for i in range(i1, i2+1):
        x[i] = y[i]
        




def mergesort_rec(x, y, i1, i2):
    """
    A recursive call to sort a subset of the array

    Parameters
    ----------
    x: list
        Array to sort
    y: list
        A temporary array / staging area to store intermediate results
    i1: int
        First index of chunk to sort, inclusive
    i2: int
        Second index of chunk to sort, inclusive (i2 >= i1)
    """
    if i2 <= i1:
        return
    mid = (i1 + i2) // 2
    mergesort_rec(x, y, i1, mid)
    mergesort_rec(x, y, mid+1, i2)
    merge(x, y, i1, mid, i2)



def mergesort(x):
    """
    An entry point for merge sort on the entire array

    Parameters
    ----------
    x: list
        Array to sort
    """
    y = [0]*len(x) # Create a temporary array to be used as a staging area
    mergesort_rec(x, y, 0, len(x)-1)


arr = [51, 21, 66, 69, 56, 13, 44, 6]
mergesort(arr)
print(arr)
arr = [23, 1, 15, 24, 47, 29]
mergesort(arr)
print(arr)
