def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def is_inorder(arr):
    """
    Parameters
    ----------
    arr: list
        An array of elements to sort
    
    Returns
    -------
    boolean: True if arr is sorted, False otherwise
    """
    inorder = True
    ## TODO: Fill this in
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            inorder = False
    return inorder

def brutesort(arr, idx=0):
    """
    Sort an array by checking all permutations
    
    Parameters
    ----------
    arr: list
        An array of elements to sort
    idx: int
        What is the index of the element we are placing in the array
    """
    if idx == len(arr)-1:
        if is_inorder(arr):
            print(arr, end='.')
    else:
        for i in range(idx, len(arr)):
            swap(arr, i, idx)
            brutesort(arr, idx+1)
            swap(arr, i, idx)

brutesort([51, 21, 66, 69, 56, 13, 44, 6])
brutesort([23, 1, 15, 24, 47, 29])