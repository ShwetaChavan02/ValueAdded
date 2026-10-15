# reverse an array in placce
# Given an array arr of n elements
# the task is to reverse the given array in-place. 
# The reversal should not create a new array; instead, it should modify the original array.

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr