"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.

Say the initial state is an array:

[1, 2, 3, 0, 4],
where 1, 2, 3, 4 are different cars, and 0 is the empty spot.

And the final state is

[0, 3, 2, 1, 4].
We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.
Each step swap with 0 only.

Edit:
Now also prints the sequence of changes in states.
Output of this example :-

initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence : 
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4
"""


def garage(initial, final):
    state = initial[:]
    while state != final:
        index_zero = state.index(0)
        num = final[index_zero]
        if num != 0:
            index_num = state.index(num)
        else:
            for i, (num1, num2) in enumerate(zip(state, final)):
                if num1 != num2:
                    num = num1
                    index_num = i
                    break
        state[index_zero] = num
        state[index_num] = 0
        yield state


def main():
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]

    print(initial)
    for state in garage(initial, final):
        print(state)


if __name__ == "__main__":
    main()
