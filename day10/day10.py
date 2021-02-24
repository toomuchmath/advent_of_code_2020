remember = {1: 1}


def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    return list(map(int, lines))


def calc_diff(sorted_numbers, diff_dict):
    left_pointer = -1
    right_pointer = 0
    length = len(sorted_numbers)

    while right_pointer < length:
        if left_pointer > -1:
            diff = sorted_numbers[right_pointer] - sorted_numbers[left_pointer]
        else:
            diff = sorted_numbers[right_pointer] - 0

        diff_dict[diff] += 1
        left_pointer += 1
        right_pointer += 1

    # the device's built-in adapter is always 3 higher than the highest adapter
    diff_dict[3] += 1

    return diff_dict


def multiply(diff):
    return diff.count(1)*(diff.count(3) + 1)


def arrangements(sorted_numbers):

    number_of_arrangements = remember.get(len(sorted_numbers))

    if number_of_arrangements is not None:
        return number_of_arrangements
    else:
        number_of_arrangements = 0

    def last_n_diff(numbers, n):
        return numbers[-1] - numbers[-n]

    diff = 0
    last_n = 2
    while diff < 3 and last_n <= len(sorted_numbers):

        diff = last_n_diff(sorted_numbers, last_n)
        if diff <= 3:
            number_of_arrangements += arrangements(sorted_numbers[:-last_n+1])
            last_n += 1
    remember[len(sorted_numbers)] = number_of_arrangements
    return number_of_arrangements


def main():
    numbers = get_input('day10.txt')

    # part 1
    sorted_numbers = sorted(numbers)
    shifted_numbers = [0] + sorted_numbers[:-1]
    zip_list = list(zip(sorted_numbers, shifted_numbers))
    diff = list(map(lambda x: x[0] - x[1], zip_list))
    print(diff)
    print(multiply(diff))

    # part 2
    device = max(sorted_numbers) + 3
    sorted_numbers = [0] + sorted_numbers
    print(sorted_numbers)
    print(arrangements(sorted_numbers))


if __name__ == '__main__':
    main()
