# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# When no character found, return letters[0]

import math

def smallest_that_is_greater(letters: list[str], target: str) -> str:
    # [letters] will always be at least length 2
    print(f"target: {target}")
    def recurse(letters: list[str], target: str, count:int=1) -> str:
        print(f"count: {count}")
        count += 1
        if count == 10:
            return

        print("in recurse")
        print(f"letters: {letters}")
        if letters[0] > target:
            print(f"first element wins: {letters[0]}")
            return letters[0]

        m = math.ceil((len(letters)-1)/2)
        print(f"m: {m}")
        if target < letters[m]:
            print(f"target {target} less than arr[m]: {letters[m]}")
            if letters[m-1] <= target:
                print(f"prev {letters[m-1]} <= target, winner: {letters[m]}")
                return letters[m]
            return recurse(letters[:m], target, count)
        
        return recurse(letters[m+1:], target, count)

    if letters[-1] <= target:
        return letters[0]
    
    return recurse(letters, target)

    



# assert smallest_that_is_greater(["c","f",/"y","y"], "z") == "x"
assert smallest_that_is_greater(["a","b","c","d","e","f"],"b") == "c"
# assert smallest_that_is_greater(["a","b","c","d","e","f"],"e") == "f"