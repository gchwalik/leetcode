# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some 
# characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

def longest_subsequence(text1: str, text2: str) -> int:
    # return len of longest common subsequence 
    len1 = len(text1)
    len2 = len(text2)
    if len1 > len2:
        str1 = text1
        str2 = text2
        str_len = len1
    else:
        str1 = text2
        str2 = text1
        str_len = len2

    i = j = count = 0 
    while i < str_len and j < str_len:
        if str1[i] == str2[j]:
            count+=1
            j+=1
        i+=1 

    return count

assert longest_subsequence("abcde", "ace") == 3
assert longest_subsequence("ace", "abcde") == 3
assert longest_subsequence("ace", "ace") == 3
assert longest_subsequence("ace", "dgh") == 0
assert longest_subsequence("psnw", "vozsh") == 1


