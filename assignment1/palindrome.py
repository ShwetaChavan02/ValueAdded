# you are given an integer n
# your task is to determine if n is a palindrome number 
# a palindrome number is one that reads the same when reversed

def is_palindrome(n):
    original_num = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return original_num == reversed_num

# def isPalindrome(n):
#     return str(n) == str(n)[::-1]