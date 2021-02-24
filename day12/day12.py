import re


def get_input(filename):
    with open(filename) as f:
        chunk = f.read()
    return chunk


def get_moves(input_chunk):
    sub_input = input_chunk.replace('L', '-').replace('R', '+')
    position_moves = re.findall(r'([NSEW][0-9]+)', sub_input)
    facing_moves = re.findall(r'([F\+\-][0-9]+)', sub_input)

    return position_moves, facing_moves


def rotate_face(instruction, move_dict):

    facing = 0
    directions = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}

    for i in instruction:

        if i[0] != 'F':
            i = int(i) // 90
            facing = (facing + i) % 4

        else:
            move_dict[directions[facing]] += int(i[1:])

    return move_dict


def move_in_direction(move_string, move_dict):

    in_dict = move_dict.get(move_string[:1])

    if not in_dict:
        move_dict[move_string[:1]] = int(move_string[1:])
    else:
        move_dict[move_string[:1]] += int(move_string[1:])

    return move_dict


def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]


def move_ship(ship_directions, waypoint_directions, instruction_value):
    for key, val in waypoint_directions.items():
        ship_directions[key] += int(instruction_value) * val
    return ship_directions


def move_waypoint(waypoint_directions, direction, value):
    waypoint_directions[direction] += int(value)
    return waypoint_directions


def rotate_waypoint(waypoint_directions, instruction):
    turn = -int(instruction) // 90
    directions = list(waypoint_directions.keys())

    shifted_directions = shift(directions, turn)

    waypoint_directions = dict(zip(shifted_directions, waypoint_directions.values()))
    return waypoint_directions


def main():
    text = get_input('day12.txt')

    # part 1
    position_moves, facing_moves = get_moves(text)
    move_dict = {}
    move_dict = list(map(lambda x: move_in_direction(x, move_dict), position_moves))[0]

    final_move_dict = rotate_face(facing_moves, move_dict)

    result = abs(final_move_dict['N'] - final_move_dict['S']) + abs(final_move_dict['E'] - final_move_dict['W'])
    print(result)

    # part 2
    replaced_text = text.replace('L', '-').replace('R', '+')

    # define starting position
    ship_directions = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    waypoint_directions = {'E': 10, 'S': 0, 'W': 0, 'N': 1}

    for instruction in replaced_text.split('\n'):

        if instruction[0] in ('E', 'S', 'W', 'N'):
            waypoint_directions = move_waypoint(waypoint_directions, instruction[0], instruction[1:])

        elif instruction[0] in ('-', '+'):
            waypoint_directions = rotate_waypoint(waypoint_directions, instruction)

        elif instruction[0] == 'F':
            ship_directions = move_ship(ship_directions, waypoint_directions, instruction[1:])

    print(waypoint_directions)
    print(ship_directions)

    result = abs(ship_directions['N'] - ship_directions['S']) + abs(ship_directions['E'] - ship_directions['W'])
    print(result)


if __name__ == '__main__':
    main()
