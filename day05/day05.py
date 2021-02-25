def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines


def to_binary(boarding_pass):
    mapper = {'F': 0, 'B': 1, 'L': 0, 'R': 1}
    reverse_string = boarding_pass[::-1]
    return [mapper[s] for s in reverse_string]


def get_seat_id(boarding_pass_binary):

    def raise_power(index):
        return 2 ** index

    raised_binaries = list(map(raise_power, [idx for idx, bi in enumerate(boarding_pass_binary) if bi != 0]))
    seat_id = sum(raised_binaries)

    return seat_id


def find_seat(seat_ids):
    for i, seat_id in enumerate(seat_ids):
        if i != (seat_id - 40):
            print(i, seat_id - 40)
            return i + 40


def main():
    boarding_passes = get_input('day05.txt')
    print(boarding_passes)
    boarding_pass_binary = list(map(to_binary, boarding_passes))
    print(boarding_pass_binary)
    seat_ids = list(map(get_seat_id, boarding_pass_binary))
    print(seat_ids)
    print(sorted(seat_ids))
    print(len(seat_ids))
    my_seat = find_seat(sorted(seat_ids))
    print(my_seat)


if __name__ == '__main__':
    main()
