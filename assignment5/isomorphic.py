# isomorphic strings
# Given two strings s and t, determine whether they are isomorphic.
# Two strings are isomorphic if every character in s can be replaced with a character 
# in t to make both strings identical, while preserving the order of characters.
# The mapping must follow these rules:
# Each character in s must always map to the same character in t.
# Two different characters in s cannot map to the same character in t.
# A character can map to itself. Return true if the strings are isomorphic; 
# otherwise, return false.

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map1 = {}
    map2 = {}
    for i in range (len(s)):
        if s[i] in map1 and map1[s[i]] != t[i]:
            return False
        if t[i] in map2 and map2[t[i]] != s[i]:
            return False
        map1[s[i]]=t[i]
        map2[t[i]]=s[i]
    return True