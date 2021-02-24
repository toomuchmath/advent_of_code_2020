def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines


def not_sum(numbers, preamble_size):

    preamble = numbers[:preamble_size]
    next_numbers = numbers[preamble_size:]
    i = 0

    for n in next_numbers:

        while True:

            if i == len(preamble):
                return n

            current = preamble[i]
            diff = n - current

            if diff in set([x for x in preamble if x != current]):
                preamble.pop(0)
                preamble.append(n)
                i = 0
                break
            else:
                i += 1


def encryption_weakness(numbers, not_sum_number):

    for i, n in enumerate(numbers):
        j = i
        total = 0
        while total < not_sum_number:
            total += numbers[j]

            if total == not_sum_number:
                return n, i, j

            j += 1


def main():
    input_list = get_input('day9.txt')
    numbers = list(map(int, input_list))

    # part 1
    not_sum_number = not_sum(numbers, 25)
    print(not_sum_number)

    # part 2
    start, start_index, end_index = encryption_weakness(numbers, not_sum_number)
    contiguous_list = numbers[start_index:end_index+1]
    print("encryption weakness:", min(contiguous_list) + max(contiguous_list))


if __name__ == '__main__':
    main()