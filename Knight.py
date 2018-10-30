"""
Imagine a knight in chess game moving on a phone dialing panel.
Starts with a digit and explores how many possible ways of dialing numbers.
"""

NEIGHBORS = {
    0: (4, 6),
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
}


def possible_ways(digit, steps):
    """
    BSF + DP:
    Calculate each digit's current state with its previous state.

    BFS gives better memory performance than DFS does in this case. DP optimizes the overall time complexity.
    """
    if digit not in NEIGHBORS:
        return 0

    pre_cache = [1] * 10
    cur_cache = [0] * 10
    cur_steps = 1

    while cur_steps <= steps:
        cur_cache = [0] * 10
        cur_steps += 1

        for i in range(0, 10):  # 10 digits
            for n in NEIGHBORS[i]:
                cur_cache[i] += pre_cache[n]
        pre_cache = cur_cache

    return cur_cache[digit]


def do_and_print(d, s):
    r = possible_ways(d, s)
    print(f'possible_ways({d}, {s}) = {r}')


do_and_print(12, 6)  # invalid digit
do_and_print(9, 0)  # no step
do_and_print(2, 1)  # 2->7 and 2->9
do_and_print(3, 6)  # 136 ways
do_and_print(5, 333)  # no way!
do_and_print(1, 10000)  # so many ways!!
