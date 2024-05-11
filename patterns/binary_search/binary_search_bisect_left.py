import bisect

def binary_search(arr: list[int], val: int) -> int:
    # returns index of val, elif val not in arr returns -1
    if arr is None:
        return -1

    i = bisect.bisect_left(arr, val)
    if i < len(arr) and arr[i] == val:
        return i
    return -1

assert binary_search(None, 4) == -1
assert binary_search([],2) == -1
assert binary_search([1], 2) == -1
assert binary_search([2],2) == 0
assert binary_search([1,2],1) == 0
assert binary_search([1,2],2) == 1
assert binary_search([1,2,3,4,5],4) == 3
assert binary_search([1,2,3,4,5],2) == 1
assert binary_search([1,2,3,4,5],100) == -1
assert binary_search([1,2,3,4,5],-13) == -1
