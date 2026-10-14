# Given an array of n elements
# the task is to return the count of the number of odd numbers in the array.

def count_odd_numbers(arr):
    count = 0
    for element in arr:
        if element % 2 != 0:
            count += 1
    return count