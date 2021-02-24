def into_list(filename):
    with open(filename) as f:
        file = f.read()
        lines = file.replace('-', ' ').replace(':', '').split('\n')

    split_lines = [x.split(' ') for x in lines]

    return split_lines


def part_one(line_list):
    valid_password_count = 0
    for line in line_list:
        at_least, at_most, char, password = [x for x in line]
        if int(at_least) <= password.count(char) <= int(at_most):
            valid_password_count += 1
    return valid_password_count


def part_two(line_list):
    valid_password_count = 0
    for line in line_list:
        index1, index2, char, password = [x for x in line]

        if password[int(index1) - 1] == char:
            if password[int(index2) - 1] != char:
                valid_password_count += 1
        else:
            if password[int(index2) - 1] == char:
                valid_password_count += 1
    return valid_password_count


if __name__ == '__main__':
    split_lines = into_list('day2.txt')
    valid_passwords = part_one(split_lines)
    print(part_two(split_lines))