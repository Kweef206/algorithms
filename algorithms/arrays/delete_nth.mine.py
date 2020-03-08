"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""
import collections


def delete_nth(lst, N):
    count = collections.defaultdict(int)

    lst_new = []
    for elm in lst:
        if count[elm] < N:
            lst_new.append(elm)
            count[elm] += 1

    return lst_new


def main():
    print(delete_nth(lst=[1, 2, 3, 1, 2, 1, 2, 3], N=2))


if __name__ == "__main__":
    main()
