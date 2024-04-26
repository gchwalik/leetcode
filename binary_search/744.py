# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# When no character found, return letters[0]

# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# When no character found, return letters[0]

import math

def smallest_that_is_greater(letters: list[str], target: str) -> str:
    # [letters] will always be at least length 2
    def recurse(letters: list[str], target: str) -> str:
        if letters[0] > target:
            return letters[0]

        m = math.ceil((len(letters)-1)/2)
        if target < letters[m]:
            if letters[m-1] <= target:
                return letters[m]
            return recurse(letters[:m], target)
        
        return recurse(letters[m+1:], target)

    if letters[-1] <= target:
        return letters[0]
    
    return recurse(letters, target)

    





assert smallest_that_is_greater(["c","f","j"], "a") == "c"
assert smallest_that_is_greater(["c","f","j"], "c") == "f"
assert smallest_that_is_greater(["x","x","y","y"], "z") == "x"
assert smallest_that_is_greater(["a","b","c","d","e","f"],"b") == "c"
assert smallest_that_is_greater(["a","b","c","d","e","f"],"e") == "f"
assert smallest_that_is_greater(
    ["p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","p","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","s","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y","y"],
    "p"
) == "r"

