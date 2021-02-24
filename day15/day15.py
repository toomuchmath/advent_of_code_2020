def get_tracking_dict(starting_numbers):
    d = dict()
    for i, n in enumerate(starting_numbers[:-1]):
        d[n] = i
    return d


def get_nth_number(starting_numbers, n):
    tracking_dict = get_tracking_dict(starting_numbers)
    starting_i = len(starting_numbers) - 1

    number = starting_numbers[-1]

    for i in range(starting_i, n):

        if i == n - 1:
            return number

        last_position = tracking_dict.get(number)
        tracking_dict[number] = i

        if last_position is not None:
            number = i - last_position
        else:
            number = 0


def main():
    starting_numbers = [17, 1, 3, 16, 19, 0]

    # part 1
    number_2020 = get_nth_number(starting_numbers, 2020)
    print(number_2020)

    # part 2
    number_30000000 = get_nth_number(starting_numbers, 30000000)
    print(number_30000000)


if __name__ == '__main__':
    main()
