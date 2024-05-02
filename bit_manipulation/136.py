# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# we know that numbers are not consecutive, so we cannot just sum
def single_number(arr: list[int]) -> int:
    def sets() -> int:
        seen = set()
        for n in arr:
            if n not in seen:
                seen.add(n)
            elif n in seen:
                seen.remove(n)
        val = seen.pop()
        return val
    
    def concise() -> int:
        # time - O(n)
        # space - O(1)
        xor = 0
        for n in arr:
            xor ^= n
        return xor
        
    return concise()

assert single_number([1]) == 1
assert single_number([4,1,2,1,2]) == 4
assert single_number([2,2,1]) == 1
