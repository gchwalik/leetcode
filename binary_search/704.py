# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def search(arr: list[int], val: int) -> int:
    # if val found, return index
    # else, return -1
    def recurse(arr: list[int], val: int, s: int, e: int, count=0):
        if s > e:
            return -1

        m = (s+e) // 2
        middle_val = arr[m]
        if middle_val == val:
            return m
        elif val > middle_val:
            return recurse(arr, val, m+1, e, count+1)
        else:
            return recurse(arr, val, s, m-1, count+1)

    return recurse(arr, val, 0, len(arr)-1)


assert search([-1,0,3,5,9,12], 3) == 2
assert search([-1,0,3,5,9,12], 9) == 4
assert search([-1,0,3,5,9,12], 2) == -1
