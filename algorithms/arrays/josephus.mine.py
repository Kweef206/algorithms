"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

[1, 2, 3, 4, 5, 6]
[1, 2, 4, 5, 6]
[1, 2, 4, 5]
[1, 2, 5]
[1, 5]
[1]
[]


def josephus(lst):
    offset = -1
    while lst:
        index = (offset + 3) % len(lst)
        print(lst.pop(index), end='')
        offset = index - 1


initial = list('123456789')
josephus(initial)
