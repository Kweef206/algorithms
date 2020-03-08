"""
Sometimes you need to limit array result to use. Such as you only need the 
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of 
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

Complexity = O(n)
"""


def limit(arr, a_min, a_max):
    arr_new = []
    for a in arr:
        if a_min is not None and a < a_min:
            continue
        if a_max is not None and a > a_max:
            continue
        arr_new.append(a)
    return arr_new


def main():
    arr_new = limit([1, 2, 3, 4, 5], None, 3)
    print(arr_new)


if __name__ == "__main__":
    main()
