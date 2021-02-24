import itertools


def get_input(filename):
    with open(filename) as f:
        rules, strings = f.read().split('\n\n')
    return rules, strings


def process(rules):
    rules = rules.replace('"', '')
    rules_list = rules.split('\n')
    rules_list = list(map(lambda x: x.split(': '), rules_list))
    rules_list = list(map(lambda x: [int(x[0]), x[1].split(' | ')], rules_list))

    return rules_list


def get_rules_dict(rules_list):
    rules_dict = {r[0]: list(map(lambda s: s.split(' '), r[1])) for r in rules_list}
    rules_dict = {n: list(map(lambda x: list(map(lambda y: int(y) if y not in 'ab' else y, x)), l)) for n, l in
                  rules_dict.items()}

    return rules_dict


def perm(list1, list2):
    return list(map(lambda t: ''.join(t), itertools.product(list1, list2)))


def get_pattern(rule_number, rules_dict, final_dict):
    final_pattern = final_dict.get(rule_number)
    if final_pattern is not None:
        return final_pattern

    final_pattern = []
    for rules in rules_dict.get(rule_number):
        pattern = ['']
        for r in rules:
            if isinstance(r, str):
                final_dict[rule_number] = [r]
                pattern += [r]
                return [r]

            pat = get_pattern(r, rules_dict, final_dict)

            pattern = perm(pattern, pat)

        final_pattern += pattern

    final_dict[rule_number] = final_pattern
    return final_dict[rule_number]


def main():
    rules, strings = get_input('day19.txt')
    rules_list = process(rules)
    rules_dict = get_rules_dict(rules_list)

    final_dict = dict()
    zero = get_pattern(0, rules_dict, final_dict)
    print(zero)

    strings_list = strings.split('\n')
    match_strings = list(filter(lambda s: s in zero, strings_list))
    print(len(match_strings))


if __name__ == '__main__':
    main()
