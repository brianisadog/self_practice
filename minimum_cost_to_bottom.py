def minimum_cost_to_bottom(array):
    """
    :type array: list[list[int]]
    :rtype: int

    Bottom up method:
    Compare left and right,
    add the small one to previous level (up)

    Each node has only to possible outcome:
    1. plus left
    2. plus right

    The left node is actually the one at
    the next level with same index.
    """
    if len(array) == 0:
        return 0

    level = len(array) - 1
    while level > 0:
        for i in range(len(array[level]) - 1):
            left = array[level][i]
            right = array[level][i + 1]

            # add to previous level
            array[level - 1][i] = array[level - 1][i] + (left if left <= right else right)

        level -= 1

    return array[0][0]  # first level item


# 30
test = [
    [2],
    [3, 4],
    [5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15, 16],
]
print(minimum_cost_to_bottom(test))

# 0
test = []
print(minimum_cost_to_bottom(test))

# 1
test = [[1]]
print(minimum_cost_to_bottom(test))

# 17
test = [
    [10],
    [33, 2],
    [43, 1, 13],
    [81, 79, 0, 9],
    [32, 13, 4, 74, 99],
]
print(minimum_cost_to_bottom(test))