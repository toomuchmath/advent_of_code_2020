import numpy as np


def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines


def to_matrix(input_lines):
    split_string = list(map(lambda s: list(s), input_lines))
    return np.array(split_string)


def check_top(matrix, i, j, initial_i=None, initial_j=None):
    if i == 0:
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i - 1][j] == '.':
        return check_top(matrix, i - 1, j, initial_i, initial_j)

    return matrix[i - 1][j] == matrix[initial_i][initial_j]


def check_bottom(matrix, i, j, initial_i=None, initial_j=None):
    rows, _ = matrix.shape
    if i == rows - 1:
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i + 1][j] == '.':
        return check_bottom(matrix, i + 1, j, initial_i, initial_j)

    return matrix[i + 1][j] == matrix[initial_i][initial_j]


def check_left(matrix, i, j, initial_i=None, initial_j=None):
    if j == 0:
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i][j - 1] == '.':
        return check_left(matrix, i, j - 1, initial_i, initial_j)

    return matrix[i][j - 1] == matrix[initial_i][initial_j]


def check_right(matrix, i, j, initial_i=None, initial_j=None):
    _, cols = matrix.shape
    if j == cols - 1:
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i][j + 1] == '.':
        return check_right(matrix, i, j + 1, initial_i, initial_j)

    return matrix[i][j + 1] == matrix[initial_i][initial_j]


def check_top_left(matrix, i, j, initial_i=None, initial_j=None):
    if (i == 0) or (j == 0):
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i - 1][j - 1] == '.':
        return check_top_left(matrix, i - 1, j - 1, initial_i, initial_j)

    return matrix[i - 1][j - 1] == matrix[initial_i][initial_j]


def check_top_right(matrix, i, j, initial_i=None, initial_j=None):
    rows, cols = matrix.shape
    if (i == 0) or (j == cols - 1):
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i - 1][j + 1] == '.':
        return check_top_right(matrix, i - 1, j + 1, initial_i, initial_j)

    return matrix[i - 1][j + 1] == matrix[initial_i][initial_j]


def check_bottom_left(matrix, i, j, initial_i=None, initial_j=None):
    rows, cols = matrix.shape
    if (i == rows - 1) or (j == 0):
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i + 1][j - 1] == '.':
        return check_bottom_left(matrix, i + 1, j - 1, initial_i, initial_j)

    return matrix[i + 1][j - 1] == matrix[initial_i][initial_j]


def check_bottom_right(matrix, i, j, initial_i=None, initial_j=None):
    rows, cols = matrix.shape
    if (i == rows - 1) or (j == cols - 1):
        return None

    if initial_i is None:
        initial_i = i

    if initial_j is None:
        initial_j = j

    if matrix[i + 1][j + 1] == '.':
        return check_bottom_right(matrix, i + 1, j + 1, initial_i, initial_j)

    return matrix[i + 1][j + 1] == matrix[initial_i][initial_j]


def check_count(matrix, i, j):

    check_list = [check_top(matrix, i, j),
                  check_bottom(matrix, i, j),
                  check_left(matrix, i, j),
                  check_right(matrix, i, j),
                  check_top_left(matrix, i, j),
                  check_top_right(matrix, i, j),
                  check_bottom_left(matrix, i, j),
                  check_bottom_right(matrix, i, j)]

    if matrix[i][j] == 'L':
        return check_list.count(True) + check_list.count(None)
    elif matrix[i][j] == '#':
        return check_list.count(True)


def flip(matrix):
    row, col = matrix.shape

    return_matrix = []

    for i in range(row):
        return_row = []
        for j in range(col):

            if matrix[i][j] == '.':
                return_row.append('.')

            elif matrix[i][j] == 'L':
                if check_count(matrix, i, j) == 8:
                    return_row.append('#')
                else:
                    return_row.append('L')

            elif matrix[i][j] == '#':
                if check_count(matrix, i, j) > 4:
                    return_row.append('L')
                else:
                    return_row.append('#')

        return_matrix.append(return_row)

    return np.array(return_matrix)


def count_seated(final_matrix):

    counter = list(map(lambda l: list(l).count('#'), final_matrix))

    return sum(counter)


def main():
    lines = get_input('day11.txt')

    matrix = to_matrix(lines)

    while True:
        return_matrix = flip(matrix)
        if np.array_equal(matrix, return_matrix):
            print(return_matrix)
            seats_occupied = count_seated(return_matrix)
            print(seats_occupied)
            break
        else:
            matrix = flip(matrix)


if __name__ == '__main__':
    main()

