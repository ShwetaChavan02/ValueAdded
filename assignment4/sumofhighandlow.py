# given an array nums of n integers,
# find the sum of the frequencies of the highest occuring number and the lowest occuring number

def sumOfFrequencies(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    highest = max(freq.values())
    lowest = min(freq.values())
    return highest + lowest
