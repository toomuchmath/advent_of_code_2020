import re


def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')

    return lines


def split_instruction(instructions):
    ops, arg = re.findall(r'(acc|jmp|nop)\s([+|-][0-9]+)', instructions)[0]
    return ops, int(arg)


def run_pointer(split_instructions):
    visited = set()
    acc_counter = 0
    pointer = 0

    while True:

        if pointer in visited:
            # print(acc_counter)            # for part 1
            break

        if pointer == len(split_instructions):
            print(acc_counter)              # for part 2
            break

        visited.add(pointer)
        ops, arg = split_instructions[pointer]

        if ops == 'acc':
            acc_counter += arg
            pointer += 1
        elif ops == 'jmp':
            pointer += arg
        elif ops == 'nop':
            pointer += 1


def switch(instruction_tuple):
    to_list = list(instruction_tuple)
    if to_list[0] == 'jmp':
        to_list[0] = 'nop'
    elif to_list[0] == 'nop':
        to_list[0] = 'jmp'
    return tuple(to_list)


def repair(split_instructions):
    for idx, instruction_pair in enumerate(split_instructions):
        ops, arg = instruction_pair
        if ops == 'acc':
            continue

        elif ops == 'jmp':
            split_instructions[idx] = switch(instruction_pair)
            run_pointer(split_instructions)
            split_instructions[idx] = switch(split_instructions[idx])

        elif ops == 'nop':
            split_instructions[idx] = switch(instruction_pair)
            run_pointer(split_instructions)
            split_instructions[idx] = switch(split_instructions[idx])


def main():
    instructions = get_input('day08.txt')
    split_instructions = list(map(split_instruction, instructions))

    # part 1
    run_pointer(split_instructions)

    # part 2
    repair(split_instructions)


if __name__ == '__main__':
    main()