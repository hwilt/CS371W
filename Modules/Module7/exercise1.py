def get_base10(x, place):
    """
    Return the digit at a particular place in a 
    base 10 number

    Parameters
    ----------
    x: int
        An integer
    place: int
        Which place to look at, where 0 is the 1s place,
        1 is the 10s place, 2 is the 100s place, etc
    """
    digit = 0
    s = "{}".format(x)
    if place < len(s):
        digit = int(s[-(1+place)])
    return digit

def radixsort(arr):
    """
    Sort an array using radix sort, assuming, for simplicity,
    that arr contains only nonnegative integers

    Parameters
    ----------
    arr: list

    """
    if len(arr) > 0:
        ## Find out the maximum number of digits needed to 
        ## represent a number in this array.  This will be
        ## the number of rounds in radix sort
        digits = 0
        for i in range(1, len(arr)):
            digits = max(digits, len("{}".format(arr[i])))

        for place in range(digits):
            staging = [0]*len(arr)
            counts = [0]*10

            ## Perform a count sort, but only using
            ## the digits at the place "place."
            for x in arr:
                d = get_base10(x, place)
                counts[d] += 1
            
            # Create an array "csum," where csum[d] holds
            # the position in the staging array where the next number
            # with digit d should be placed in the staging area.
            # For instance, if there are 5 numbers with digit 0 and
            # 3 numbers with digit 1, the first number with a digit 2
            # should be placed at index 8
            csum = [0]*10
            for i in range(1, 10):
                csum[i] = csum[i-1] + counts[i-1]
            
            ## Loop through arr.  For each element x, get the 
            ## digit d at the current place, put that element
            ## in the staging area according to csum[d], and
            ## then increment csum[d] so we know where to place
            ## the next element with digit d
            for x in arr:
                d = get_base10(x, place)
                ## TODO: Finish this
                staging[csum[d]] = x
                csum[d] += 1
            
            # Copy elements back from the staging area into arr
            for i in range(len(arr)):
                arr[i] = staging[i]

arr = [684, 559, 629, 192, 835, 763, 707, 359, 9, 723, 277, 754, 804, 599, 70, 472, 600, 396, 314, 705]
radixsort(arr)
print(arr, end='.')
arr = [37, 235, 908, 72, 767, 905, 715, 645, 847, 960, 144, 129, 972, 583, 749, 508, 390, 281, 178, 276]
radixsort(arr)
print(arr)