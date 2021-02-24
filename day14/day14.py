import re


def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('mask = ')

    lines = [li for li in lines if li != '']
    lines = list(map(lambda l: l.split('\n'), lines))

    return lines


def memory_list(memory):
    i = re.findall(r'mem\[([0-9]+)\] \= ([0-9]+)$', memory)
    return i[0]


def pad_string(binary, mask):
    length = max(len(max(binary)), len(mask))

    return list(map(lambda b: b.zfill(length), binary)), mask.zfill(len(max(binary)))


def replace_memory(mask, bin_memory):
    new_bin_memory = []
    for idx, m in enumerate(mask):
        if m == 'X':
            new_bin_memory.append(bin_memory[idx])
        else:
            new_bin_memory.append(m)

    return ''.join(new_bin_memory)


def replace_character(string, index, to_be_replaced):
    reversed_string = string[::-1]
    replaced_reverse = reversed_string[:index] + to_be_replaced + reversed_string[index + 1:]
    return replaced_reverse[::-1]


def part1(groups):
    d = dict()

    for group in groups:
        mask = group[0]
        memory = group[1:]
        memory = list(filter(None, memory))

        effective_mask = re.findall(r'X*(.+)$', mask)[0]
        memory_tuples = list(map(memory_list, memory))

        binary = list(map(lambda m: '{0:b}'.format(int(m[1])), memory_tuples))
        binary, effective_mask = pad_string(binary, effective_mask)

        new_binary = list(map(lambda b: replace_memory(effective_mask, b), binary))
        new_int = list(map(lambda x: int(x, 2), new_binary))
        memory_int = [(int(memory_tuples[i][0]), new_int[i]) for i in range(len(memory_tuples))]

        for m in memory_int:
            d[m[0]] = m[1]

    return d


def part2(groups):
    d = dict()

    for group in groups:
        mask = group[0]
        memory = group[1:]
        memory = list(filter(None, memory))

        memory_tuples = list(map(memory_list, memory))
        space_binary = list(map(lambda t: '{0:b}'.format(int(t[0])).zfill(len(mask)), memory_tuples))

        additions = [0]
        for idx, m in enumerate(mask[::-1]):
            if m == 'X':
                space_binary = list(map(lambda s: replace_character(s, idx, '0'), space_binary))
                add = [2 ** idx + x for x in additions]
                additions.extend(add)
            elif m == '1':
                space_binary = list(map(lambda s: replace_character(s, idx, '1'), space_binary))

        binary_memory_tuple = list(zip(space_binary, [t[1] for t in memory_tuples]))

        for memory in binary_memory_tuple:
            add_spaces = [int(memory[0], 2) + add for add in additions]
            for space in add_spaces:
                d[space] = int(memory[1])

    return d


def main():
    groups = get_input('day14.txt')

    # part 1
    part1_dict = part1(groups)
    print(sum(part1_dict.values()))

    # part 2
    part2_dict = part2(groups)
    print(sum(part2_dict.values()))


if __name__ == '__main__':
    main()