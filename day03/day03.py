def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')

    return lines


def coordinates(row, x_increment, y_increment):
    y = row * y_increment
    x = (row * x_increment) % 31

    return x, y


def count_trees(split_lines, x_increment, y_increment):

    row_count = len(split_lines)
    number_of_trees = 0

    for i in range(1, row_count):
        x, y = coordinates(i, x_increment, y_increment)
        if y >= len(split_lines):
            break
        if split_lines[y][x] == '#':
            number_of_trees += 1

    return number_of_trees


def main():
    split_lines = get_input('day03.txt')
    number_of_trees11 = count_trees(split_lines, 1, 1)
    number_of_trees31 = count_trees(split_lines, 3, 1)
    number_of_trees51 = count_trees(split_lines, 5, 1)
    number_of_trees71 = count_trees(split_lines, 7, 1)
    number_of_trees12 = count_trees(split_lines, 1, 2)
    print(number_of_trees11*number_of_trees31*number_of_trees51*number_of_trees71*number_of_trees12)


if __name__ == '__main__':
    main()

    # shape of input is (323, 31)