# check if array is sorted 
# Given an array arr of size n
# the task is to check if the given array is sorted in ascending order. 
# If the array is sorted, return True; otherwise, return False.

def isArraySorted(n, arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True