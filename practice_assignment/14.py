# palindrom enumber
# You are given an integer n. 
# Your task is to determine if n is a palindrome number. 
# A palindrome number is one that reads the same when reversed.

def isPalindrome(n):
    return str(n) == str(n)[::-1]