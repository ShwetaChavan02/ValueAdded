# longest common prefix
# Given an array of strings str, find the longest common prefix shared by all the strings in the array.
# A prefix is a sequence of characters that appears at the beginning of a string.
# If there is no common prefix among all the strings, return an empty string "".

def longestCommonPrefix(str: list[str]) -> str:
    if not str:
        return ""
    prefix = str[0]
    for word in str[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix