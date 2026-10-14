# Given an array arr of n elements
# the task is to reverse the given array in-place.
# The reversal should not create a new array; instead, it should modify the original array.

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr