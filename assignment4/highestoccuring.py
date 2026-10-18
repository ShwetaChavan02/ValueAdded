# highest occuring element
# given an array nums of n integers, find the most frequent element in it
# the elemenet that occures the maximum number of times is called the most frequent element
# if there are multiple elements that appear a maximum number of times, return the smallest one


def highestOccurringElement(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    result=[]
    for num in freq:
        if freq[num]==max_freq:
            result.append(num)
    return min(result) 