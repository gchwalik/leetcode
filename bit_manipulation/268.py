# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

from datetime import datetime, timedelta

def missing_num(arr: list[int]) -> int:
    def xor() -> int:
        actual = 0
        for val in arr:
            actual ^= val
        full = 0 
        for val in range(len(arr)+1):
            full ^= val
        return full ^ actual

    def xor2() -> int:
        actual = full = 0
        n = len(arr)
        for i in range(n):
            actual ^= arr[i]
            full ^= i
        full ^= n
        return full ^ actual

    def sums() -> int:
        # full = sum(range(len(arr)+1))
        n = len(arr)
        full = n*(n+1)/2
        actual = sum(arr)
        return full - actual

    return xor2()

def tests() -> None:
    assert missing_num([0]) == 1
    assert missing_num([0,1,2,3]) == 4
    assert missing_num([1,0,4,3]) == 2
    assert missing_num([2,4,3,1]) == 0
    assert missing_num([n for n in range(1000) if n != 376]) == 376

def test_harness() -> float:
    total_sec = 0
    for _ in range(20000):
        start = datetime.now()
        tests()
        stop = datetime.now()
        total_sec += (stop-start).total_seconds()
    print(f"sums: {total_sec}")

test_harness()