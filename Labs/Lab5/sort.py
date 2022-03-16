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
    ## TODO: Fill this in


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
    ## TODO: Fill this in



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
