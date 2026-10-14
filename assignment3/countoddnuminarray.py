# Given an array of n elements
# the task is to return the count of the number of odd numbers in the array.

def isArraySorted(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True