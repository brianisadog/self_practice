def read_file(filename):
    """
    :type filename: str
    :rtype: list
    """
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            matrix.append([int(num) for num in line.split()])
    return matrix


def shortest_path(m, start, destination):
    """
    :type m: list
    :type start: chr
    :type destination: chr
    :rtype: list

    Matrix contains an n*n matrix indicates duration between two locations.
    There are 8 locations A~H indicate the indexes 0~7 in the matrix.
    The row indicates "from", and the column indicates "to".
    For example, matrix[3][6] = 10: The duration from location [D] to location [F] is 10.

    Return all possible paths from start node to destination node,
    sorted from shortest duration to longest.
    """
    if len(start) != 1 or len(destination) != 1:
        print('Illegal arguments.')
        return []

    a = convert_to_int(start)
    b = convert_to_int(destination)

    if a not in range(len(m)) or b not in range(len(m)):
        print('Out of range.')
        return []

    duration = []
    path = []
    visited = [False for _ in range(len(m))]

    dfs(m, a, b, duration, path, visited, 0, '')
    combine = sorted(zip(duration, path))  # combine two list together and sort base on the duration

    return combine


def dfs(m, current, b, duration, path, visited, current_dur, current_path):
    """
    Keep visiting node, that is reachable (duration != 0) and has not been visited, until hit the destination.
    """
    visited[current] = True
    current_path += convert_to_chr(current) + '->'

    if current == b:
        duration.append(current_dur)
        path.append(current_path[:-2])  # remove arrow in the end
        return

    current_row = m[current]
    for i in range(len(current_row)):
        if current_row[i] != 0 and not visited[i]:
            dfs(m, i, b, duration, path, visited, current_dur + current_row[i], current_path)
            visited[i] = False  # need to reset visited since Python is pass by value to the actual object.


def convert_to_int(char):
    """
    :type char: chr
    :rtype: int

    Convert character into integer, starts from 'A' = 0.
    """
    return ord(char.upper()) - ord('A')


def convert_to_chr(i):
    return chr(ord('A') + i)


m = read_file('files/route.txt')

result = shortest_path(m, 'A', 'B')
print('Find path A->B:')
print(result)

print()

print('Find path C->H:')
result = shortest_path(m, 'C', 'H')
print(result)

print()

print('Find path E->F:')
result = shortest_path(m, 'E', 'F')
print(result)

print()

print('Find path A->R:')
result = shortest_path(m, 'A', 'R')
print(result)

print()

print('Find path AB->D:')
result = shortest_path(m, 'AB', 'D')
print(result)
