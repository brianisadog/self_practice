def is_toeplitz_matrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool

    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
    Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
    """
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


def is_toeplitz_matrix_1(matrix, k):
    """
    Follow up: What if the matrix is so large that you can only load up a partial row into the memory at once?

    My solution:
    Load k rows a time and compare only between these k rows, overlap the first row with the previous last row.
    len(matrix) >= k >= 2, k is the maximum row number that our memory can handle for loading partial matrix.
    """
    def get_k_row_start_from_i(m, i, k):
        return m[i:i + k]

    # step k - 1 since we are overlapping the first row with the previous last row.
    for i in range(0, len(matrix) - 1, k - 1):
        m = get_k_row_start_from_i(matrix, i, k)
        if not is_toeplitz_matrix(m):
            return False
    return True


# True
test_l = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
print(is_toeplitz_matrix(test_l))
print(is_toeplitz_matrix_1(test_l, 2))

print()

# False
test_l = [[1, 2], [2, 2]]
print(is_toeplitz_matrix(test_l))
print(is_toeplitz_matrix_1(test_l, 2))

print()

# True
test_l = [[18], [66]]
print(is_toeplitz_matrix(test_l))
print(is_toeplitz_matrix_1(test_l, 2))

print()

# True
test_l = [
    [1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5],
    [9, 0, 1, 2, 3, 4],
    [8, 9, 0, 1, 2, 3],
    [7, 8, 9, 0, 1, 2],
]
print(is_toeplitz_matrix(test_l))
print(is_toeplitz_matrix_1(test_l, 4))

print()

# False
test_l = [
    [1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5],
    [9, 0, 1, 4, 3, 4],
    [8, 9, 0, 1, 2, 3],
    [7, 8, 9, 0, 1, 2],
]
print(is_toeplitz_matrix(test_l))
print(is_toeplitz_matrix_1(test_l, 3))
