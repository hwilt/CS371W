import numpy as np
np.random.seed(0) # to easily keep the results the same

def binarysearch(arr, target, low=0, high=-1):
	"""
	arr: list
		A sorted array of numbers
	target: float
		A target number
	low: int
		Low index of range to check
	high:
		High index of range to check

	Returns
	-------
	Index of one of the occurrences of target if it exists in
	the array, or -1 otherwise
	"""
	if high == -1:
		high = len(arr)-1 # Start off all the way to the right
	res = -1
	if low == high:
		if arr[low] == target:
			res = low
	else:
		mid = (low+high)//2
		if arr[mid] < target:
			res = binarysearch(arr, target, mid+1, high)
		else:
			res = binarysearch(arr, target, low, mid)
	return res

		
	
"""
def binarysearch(arr, target):
	" ""
	arr: list
		A sorted array of numbers
	target: float
		A target number

	Returns
	-------
	Index of one of the occurrences of target if it exists in
	the array, or -1 otherwise
	" ""
	ret = -1
	high = len(arr)-1
	low = 0
	while low <= high:
		mid = (low+high)//2
		if arr[mid] == target:
			ret = mid
			low = high+1
		elif arr[mid] > target:
			high = mid-1
		else:
			low = mid+1
	return ret
"""		
		
arr = sorted(np.random.randint(0,100,70))
#print(arr)

for i in range(100):
	binaryreturn = binarysearch(arr, i)
	if(binaryreturn == -1):
		print(i, "-1")
	else:
		print(i, binaryreturn, arr[binaryreturn])