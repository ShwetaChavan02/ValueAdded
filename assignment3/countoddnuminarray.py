# Given an array of n elements
# the task is to return the count of the number of odd numbers in the array.

def count_odd_numbers(n, arr):
    count = 0
    for i in range(n):
        if arr[i] % 2 != 0:
            count += 1
    return count