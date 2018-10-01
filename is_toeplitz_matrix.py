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


test_l = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
print(is_toeplitz_matrix(test_l))

test_l = [[1, 2], [2, 2]]
print(is_toeplitz_matrix(test_l))

test_l = [[18], [66]]
print(is_toeplitz_matrix(test_l))
