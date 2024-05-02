# An array arr is a mountain if the following properties hold:
# - arr.length >= 3
# - there exists some i with 0 < i < arr.length - 1 such that:
#   - arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#   - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.



def get_peak_index(arr: list[int]) -> int:
    # m - array of ints describing the shape of the mountain 
    # start and end cannot be the peak 
    def get_slice(m:int) -> list[int]:
        # [0,1,2,3,4,5], m=2
        # return [1,2,3]
        return arr[m-1:m+2]

    def get_slope(m: int) -> int:
        slice = get_slice(m)
        s, m, e = slice
        if s > m:
            return -1
        if e > m:
            return 1
        return 0

    def recurse(s: int, e: int) -> int:
        # returns index of mountain peak 
        m = (s+e) // 2
        slope = get_slope(m)
        if slope == 0:
            return m
        elif slope > 0:
            # mountain rising, so slice to the right
            return recurse(m, e)
        else:
            # mountain falling, so slice to the left
            return recurse(s, m)

    def loop() -> int:
        s, e = [0, len(arr)-1]
        m = (e-s) // 2
        while arr[m-1] > arr[m] or arr[m+1] > arr[m]:
            # second case is s<m and e>m, mountain rising
            if arr[m-1] > arr[m]:
                # mountain falling
                e=m
            if arr[m+1] > arr[m]:
                # mountain fallling
                s=m
            m = (s+e) // 2
        return m

    return loop()
    # return recurse(0, len(arr)-1)


assert get_peak_index([0,1,0]) == 1
assert get_peak_index([0,1,2,0]) == 2
assert get_peak_index([0,10,5,2]) == 1






