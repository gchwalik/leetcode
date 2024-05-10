def binary_search(arr: list[int], target: int) -> int:
    # returns index of target, returns -1 if not found
    def recurse(low: int, high: int) -> int:
        # returns index of target, returns -1 if not found
        if target < arr[low] or target > arr[high]:
            return -1
        if high == low:
            return 0 if arr[low] == target else -1
        if arr[low] == target:
            return low
        if arr[high] == target:
            return high 
        mid = (low+high) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val > target:
            return recurse(low, mid-1)
        else: # mid_val < target
            return recurse(mid+1, high)
    
    # None or []
    if not arr:
        return -1
    return recurse(0, len(arr)-1)

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