# given an array nums of n integers, find the second most frequent element in it
# the elemenet that occures the maximum number of times is called the most frequent element
# if there are multiple elements that appear a maximum number of times, return the smallest one
# if the second most frequent element is not present, return -1

def secondHighestOccurringElement(arr):
    if isinstance(arr, int):
        return -1
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    frequencies = sorted(set(freq.values()),reverse=True)
    if len(frequencies) < 2:
        return -1
    second_freq = frequencies[1]
    result = []
    for num in freq:
        if freq[num] == second_freq:
            result.append(num)
    return min(result)