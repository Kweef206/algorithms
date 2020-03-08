"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable


def flatten(lst):
    lst_new = []
    for elm in lst:
        if isinstance(elm, Iterable):
            lst_new.extend(flatten(elm))
        else:
            lst_new.append(elm)
    return lst_new


def main():
    nested_array = [1, [2, 3], [4, [5, 6, [7]]], [8]]
    print(flatten(nested_array))


if __name__ == "__main__":
    main()
