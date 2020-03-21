"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""

def missing_ranges(arr, low, high):
    res = []
    start = low
    for n in arr:
        if n == low:
            start += 1
        else:
            res.append((start, n - 1))
            start = n + 1
    if n != high:
        res.append((start, high))
    return res


print(missing_ranges([3, 5], 1, 10))
print(missing_ranges([3, 10], 1, 10))
print(missing_ranges([3, 9], 1, 10))
print(missing_ranges([1, 3, 9], 1, 10))
