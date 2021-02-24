import re


def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines


##########
# PART 1 #
##########

def into_dict(rules_list):
    rules_dict = dict(rule.split(" contain ") for rule in rules_list)

    def to_bag_list(rule_string):
        bags = re.findall(r"(\w+\s\w+)\sbags?", rule_string)
        if 'no other' in bags:
            bags.remove('no other')
        return bags

    rule_nested_dict = dict()

    for key, val in rules_dict.items():
        rule_nested_dict[key] = to_bag_list(val)

    return rule_nested_dict


def bag_colours(rule_nested_dict):
    bags = dict()

    for key, val in rule_nested_dict.items():
        for v in val:
            if v not in bags.keys():
                bags[v] = [key[:-5]]
            else:
                bags[v].append(key[:-5])

    return bags


def dfs(visited, bag_graph, node):
    if node not in visited:
        visited.add(node)
        if node in bag_graph.keys():
            for neighbour in bag_graph[node]:
                dfs(visited, bag_graph, neighbour)
        else:
            pass
    return visited


##########
# PART 2 #
##########

def count_colours(rules_list):
    rules_dict = dict(rule.split(" contain ") for rule in rules_list)

    def to_bag_list(rule_string):
        bags = re.findall(r"([0-9]) (\w+\s\w+)\sbags?", rule_string)
        if 'no other' in bags:
            bags.remove('no other')
        return bags

    rule_nested_dict = dict()

    for key, val in rules_dict.items():
        rule_nested_dict[key[:-5]] = to_bag_list(val)

    return rule_nested_dict


def dfs_sum(bag_count_dict, bag_colour):
    total = 0
    if bag_count_dict[bag_colour]:
        for bag in bag_count_dict[bag_colour]:
            total += int(bag[0]) * (dfs_sum(bag_count_dict, bag[1]) + 1)
    else:
        for bag in bag_count_dict[bag_colour]:
            total = int(bag[0])

    return total


def main():
    rules = get_input('day7.txt')

    # part 1
    rule_nested_dict = into_dict(rules)
    bag_graph = bag_colours(rule_nested_dict)

    visited = set()
    visited_nodes = dfs(visited, bag_graph, 'shiny gold')
    print(len(visited_nodes) - 1)       # excluding the shiny gold bag itself

    # part 2
    bag_count_dict = count_colours(rules)
    total = dfs_sum(bag_count_dict, 'shiny gold')
    print(total)


if __name__ == '__main__':
    main()
