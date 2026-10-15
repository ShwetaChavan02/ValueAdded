# count odd numbers in an array
# Given an array of n elements
# the task is to return the count of the number of odd numbers in the array.

def count_odd_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count