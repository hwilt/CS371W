def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def insertionsort(arr, idx=0):
    """
    Sort an array via the insertion sort algorithm
    
    Parameters
    ----------
    arr: list
        An array of elements to sort
    """
    for i in range(1, len(arr)):
        j = i
        # As long as j > 0 and 
        # arr[j] < arr[j-1], swap 
        # the indices j and j-1 and decrement j
        while j > 0 and arr[j] < arr[j-1]:
            swap(arr, j, j-1)
            j -= 1
            

arr = [51, 21, 66, 69, 56, 13, 44, 6]
insertionsort(arr)
print(arr, end='.')
arr = [23, 1, 15, 24, 47, 29]
insertionsort(arr)
print(arr)