import re
from intervaltree import Interval, IntervalTree
import numpy as np
import math
from functools import reduce


def get_input(filename):
    with open(filename) as f:
        fields, my_ticket, nearby_tickets = f.read().split('\n\n')
    return fields, my_ticket, nearby_tickets


def extract_field_range(fields):
    field_range = re.findall(r'([0-9]+)\-([0-9]+)', fields)

    return field_range


def extract_nearby_tickets(nearby_tickets):
    nearby_tickets = nearby_tickets.split('\n')[1:]
    nearby_tickets = list(map(lambda ticket: ticket.split(','), nearby_tickets))

    return nearby_tickets


def part1(nearby_tickets, my_ticket, tree):

    invalid = []
    nearby_tickets = extract_nearby_tickets(nearby_tickets)
    my_ticket = my_ticket.split('\n')[1:]
    my_ticket = [string.split(',') for string in my_ticket][0]

    for tickets in nearby_tickets:
        for t in tickets:
            if len(tree[int(t)]) == 0:
                invalid.append(int(t))
            else:
                continue

    # print(invalid)
    # print(sum(invalid))

    return nearby_tickets, my_ticket


def get_valid_tickets(nearby_tickets, tree):

    return filter(lambda ticket: all(map(lambda t: len(tree[int(t)]) > 0, ticket)), nearby_tickets)


def part2(nearby_tickets, my_ticket, all_trees, field_range):

    # part 2
    valid_tickets = get_valid_tickets(nearby_tickets, all_trees)

    valid_tickets_col = list(zip(*valid_tickets))

    range_count = len(field_range)
    condition_match = []

    for i in range(0, range_count, 2):
        tree_range = [(int(field_range[i][0]), int(field_range[i][1]) + 1),
                      (int(field_range[i + 1][0]), int(field_range[i + 1][1]) + 1)]
        # print(tree_range)

        tree = IntervalTree.from_tuples(tree_range)

        result = list(map(lambda valid: all([len(tree[int(n)]) > 0 for n in valid]), valid_tickets_col))
        # print(result)
        # print(list(np.where(result)[0]))
        condition_match.append(list(np.where(result)[0]))

    sorted_condition_match = sorted(condition_match, key=len)
    sorted_index = list(map(condition_match.index, sorted_condition_match))

    print("conditions satisfied by each column: ", condition_match)
    print("conditions satisfied by each column, sorted by length: ", sorted_condition_match)
    print("positions in the original list with respect to the sorted list", sorted_index)

    # result = [sorted_condition_match[0]]
    # for i in range(len(sorted_condition_match) - 1):
    #     result.append(set(sorted_condition_match[i+1]) - set(sorted_condition_match[i]))
    # print(result)

    final_cond = []
    for possible_conditions in sorted_condition_match:
        for cond in possible_conditions:
            if cond not in final_cond:
                final_cond.append(cond)
                break

    print(len(field_range)/2)
    print(len(final_cond))
    print(final_cond)

    column_conditions = list(zip(sorted_index, final_cond))
    # print(respective_i)
    conditions_list = list(map(lambda t: t[1], sorted(column_conditions, key=lambda x: x[0])))
    print("columns in the condition order", list(map(lambda t: t[0], sorted(column_conditions, key=lambda x: x[1]))))
    print("conditions in the column order", list(map(lambda t: t[1], sorted(column_conditions, key=lambda x: x[0]))))

    departure_cols = conditions_list[:6]
    print(departure_cols)
    numbers = list(map(lambda x: int(my_ticket[x]), departure_cols))
    print(numbers)

    print(math.prod(numbers))


def main():
    fields, my_ticket, nearby_tickets = get_input('day16.txt')

    field_range = extract_field_range(fields)

    tree = IntervalTree(Interval(int(begin), int(end) + 1, (int(begin), int(end) + 1)) for begin, end in field_range)
    nearby_tickets, my_ticket = part1(nearby_tickets, my_ticket, tree)
    part2(nearby_tickets, my_ticket, tree, field_range)


if __name__ == '__main__':
    main()
