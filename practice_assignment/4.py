# sum of array elements
# Given an array arr of size n
# your task is to find the sum of all the elements in the array.

def sum_of_array_elements(n, arr):
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum