def into_list(filename):
    with open(filename) as f:
        numbers = f.read().split('\n')
        numbers = list(map(int, numbers))
        return numbers


def multiply(input_list, result):

    input_set = set(input_list)

    for x in input_list:
        target = result - x
        if target in input_set:
            return x * target


def three_numbers(input_list):

    for x in input_list:
        diff = 2020 - x
        reduced_list = [x for x in input_list if x < diff]
        reduced_set = set(input_list)
        for y in reduced_list:
            target = diff - y
            if target in reduced_set:
                return x * y * target


if __name__ == '__main__':
    print(three_numbers(into_list('day1.txt')))

