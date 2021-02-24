from functools import reduce


def get_input(filename):
    with open(filename) as f:
        initial_states = f.read().split('\n')

    active_states = set()
    for i, row in enumerate(initial_states):
        for j, state in enumerate(row):
            if state == '#':
                active_states.add((i, j, 0))

    return active_states


def get_input_4d(filename):
    with open(filename) as f:
        initial_states = f.read().split('\n')

    active_states = set()
    for i, row in enumerate(initial_states):
        for j, state in enumerate(row):
            if state == '#':
                active_states.add((i, j, 0, 0))

    return active_states


def neighbouring_coordinates(current_coordinates):
    x, y, z = current_coordinates
    neighbours = [(x - 1 + i, y - 1 + j, z - 1 + k) for i in range(3) for j in range(3) for k in range(3)]
    neighbours.remove(current_coordinates)

    return neighbours


def neighbouring_coordinates_4d(current_coordinates):
    w, x, y, z = current_coordinates
    neighbours = [(w - 1 + i, x - 1 + j, y - 1 + k, z - 1 + l) for i in range(3) for j in range(3) for k in range(3) for l in range(3)]
    neighbours.remove(current_coordinates)

    return neighbours


def part1():
    active_states = get_input('day17.txt')

    cycle = 1
    while cycle < 7:
        print(active_states)
        new_active_states = set()
        neighbour_coordinates = list(map(lambda c: neighbouring_coordinates_4d(c), list(active_states)))

        # un-nest the previous list
        all_neighbours = reduce(lambda x, y: x + y, neighbour_coordinates)
        neighbour_count = dict((x, all_neighbours.count(x)) for x in set(all_neighbours))
        consider_coordinates = {k: v for k, v in neighbour_count.items() if v in (2, 3)}

        for coordinates, count in consider_coordinates.items():
            if count == 3:
                new_active_states.add(coordinates)
            elif count == 2:
                if coordinates in active_states:
                    new_active_states.add(coordinates)
        active_states = new_active_states
        cycle += 1

    print(len(new_active_states))


def part2():
    active_states = get_input_4d('day17.txt')
    cycle = 1
    while cycle < 7:
        print(active_states)
        new_active_states = set()
        neighbour_coordinates = list(map(lambda c: neighbouring_coordinates_4d(c), list(active_states)))

        # un-nest the previous list
        all_neighbours = reduce(lambda x, y: x + y, neighbour_coordinates)
        neighbour_count = dict((x, all_neighbours.count(x)) for x in set(all_neighbours))
        consider_coordinates = {k: v for k, v in neighbour_count.items() if v in (2, 3)}

        for coordinates, count in consider_coordinates.items():
            if count == 3:
                new_active_states.add(coordinates)
            elif count == 2:
                if coordinates in active_states:
                    new_active_states.add(coordinates)
        active_states = new_active_states
        cycle += 1

    print(len(new_active_states))


def main():

    # part1()
    part2()


if __name__ == '__main__':
    main()