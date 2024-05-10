

def binary_search(arr: list[int], target: int) -> int:
    # returns index of target, if not found returns -1
    def recurse(low: int, high: int) -> int:
        # returns index of target, if not found returns -1
        if low > high:
            return -1 
        mid = (low+high) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val > target:
            return recurse(low, mid-1)
        else: # mid_val < target
            return recurse(mid+1, high)

    if not arr:
        return -1 
    return recurse(0, len(arr)-1)

assert binary_search(None, -2) == -1
assert binary_search([], 3) == -1
assert binary_search([1], 1) == 0
assert binary_search([1], 2) == -1
assert binary_search([1,2],1) == 0
assert binary_search([1,2],2) == 1
assert binary_search([1,2,3,4,5,6,7], 6) == 5
assert binary_search([1,2,3,4,5,6,7], 3) == 2
assert binary_search([1,2,3,4,5,6,7], -1) == -1
assert binary_search([1,2,3,4,5,6,7], 13) == -1
