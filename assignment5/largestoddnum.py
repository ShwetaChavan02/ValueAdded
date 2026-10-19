# largest odd number in a string
# Given a string s representing a non-negative integer, 
# find the largest-valued odd number that can be obtained as a substring of s.
# The returned number must be a string and must not contain leading zeros. 
# If no odd number exists, return an empty string "".
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def largestOddNumber(self, s: str):
        n = int(s)
        while n > 0:
            if n % 2 != 0:
                return n
            n //= 10
        return ""

