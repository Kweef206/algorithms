"""
Find the index of 0 to be replaced with 1 to get
longest continuous sequence
of 1s in a binary array.
Returns index of 0 to be
replaced with 1 to get longest
continuous sequence of 1s.
If there is no 0 in array, then
it returns -1.

e.g.
let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
"""


def max_ones_index(arr):
    index_and_length = {}
    index_0 = -1
    for index_i, elem in enumerate(arr):
        if elem == 0:
            # stop all previous 1s
            for index_j in index_and_length:
                length, is_stopped = index_and_length[index_j]
                index_and_length[index_j] = (length, True)

            index_and_length[index_i] = (index_i - index_0, False)
            index_0 = index_i
        elif elem == 1:
            if index_i == 0:
                index_and_length[index_i] = (1, False)
            else:
                for index_j in index_and_length:
                    length, is_stopped = index_and_length[index_j]
                    # increment 1s
                    if not is_stopped:
                        index_and_length[index_j] = (length + 1, False)
        else:
            raise ValueError
    return max(index_and_length.items(), key=lambda x: x[1][0])[0]


if __name__ == "__main__":
    arr = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    print(max_ones_index(arr))
