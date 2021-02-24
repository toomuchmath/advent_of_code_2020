from functools import reduce


def get_input(filename):
    with open(filename) as f:
        earliest, buses = f.read().split('\n')

    return earliest, buses


def to_int(earliest, buses):
    buses = [bus for bus in buses.split(',') if bus != 'x']

    earliest = int(earliest)
    buses = list(map(int, buses))
    return earliest, buses


def get_next_bus(earliest, bus_number):
    multiplier = earliest // bus_number

    if earliest % bus_number > 0:
        return (multiplier + 1) * bus_number

    else:
        return earliest


def extended_euclid(a, b):

    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda c, d: c * d, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * extended_euclid(p, n_i) * p
    return sum % prod


def main():
    earliest, buses = get_input('day13.txt')

    # part 1
    earliest, buses = to_int(earliest, buses)
    next_buses = list(map(lambda b: get_next_bus(earliest, b), buses))
    wait_time = list(map(lambda b: b - earliest, next_buses))

    min_wait_time = min(wait_time)
    bus = buses[wait_time.index(min_wait_time)]
    print(bus * min_wait_time)

    # part 2
    _, buses = get_input('day13.txt')

    buses = [bus for bus in buses.split(',')]
    working_buses = [int(bus) for bus in buses if bus != 'x']
    remainder = [(bus - buses.index(str(bus))) % bus for bus in working_buses]

    print(chinese_remainder(working_buses, remainder))


if __name__ == '__main__':
    main()
