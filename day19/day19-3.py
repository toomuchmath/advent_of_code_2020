import re


def get_input(filename):
    with open(filename) as f:
        rules, strings = f.read().split('\n\n')
    return rules, strings


def get_rules_dict(rules):

    rules = rules.replace('"', '')
    rules_dict = dict(x.split(": ") for x in rules.split("\n"))
    # rules_dict = {int(k): v for k, v in rules_dict.items()}

    return rules_dict


def sub_regex(rules_dict):
    for k, v in rules_dict.items():
        match = re.sub(r'(\d)', rules_dict[r'\1'], v)
        print(match)


def main():
    rules, strings = get_input('day19.txt')
    print(rules)
    print(strings)

    rules_dict = get_rules_dict(rules)
    print(rules_dict)

    sub_regex(rules_dict)


if __name__ == '__main__':
    main()