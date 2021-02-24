import re


def get_input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    without_spaces = list(map(lambda s: s.replace(' ', ''), lines))
    return without_spaces


def satisfy(condition):
    def parser(string):
        if len(string) == 0:
            return None
        elif condition(string[0]):
            return string[0], string[1:]
        else:
            return None
    return parser


def sequence(parser1, parser2):
    def parser(string):
        result1 = parser1(string)
        if result1 is None:
            return None
        target1, remainder1 = result1
        result2 = parser2(remainder1)
        if result2 is None:
            return None
        target2, remainder2 = result2
        return (target1, target2), remainder2
    return parser


def times(parser):
    def f(string):
        targets = []
        while True:
            result = parser(string)
            if result is None:
                return targets, string
            target, remainder = result
            targets.append(target)
            string = remainder
    return f


def choice(parser1, parser2):
    def parser(string):
        result1 = parser1(string)
        if result1 is not None:
            return result1
        return parser2(string)
    return parser


def apply(f, parser):
    def g(string):
        result = parser(string)
        if result is None:
            return None
        target, remainder = result
        return f(target), remainder
    return g


def plus(parser):
    return apply(lambda x: [x[0]] + x[1], sequence(parser, times(parser)))


def binding():
    x = [lambda x: x]

    def bind(y):
        x[0] = y

    def parser(string):
        return x[0](string)

    return bind, parser


def evaluate(x):
    value, operators = x
    result = value
    for operator, value in operators:
        if operator == '+':
            result += value
        elif operator == '-':
            result -= value
        elif operator == '*':
            result *= value
        elif operator == '/':
            result /= value
    return result


def main():

    number = satisfy(lambda x: x in '0123456789')
    big_number = apply(lambda li: int(''.join(li)), plus(number))

    """
    Expr        ← Sum (('-' / '*' / '/') Sum)*
    Sum         ← Value ('+' Value)*
    Value       ← BigNumber / '(' Expr ')'
    BigNumber   ← [0-9]+
    """

    # part 1
    # bind, expression = binding()
    # value = choice(big_number, apply(lambda x: x[1], sequence(satisfy(lambda x: x == '('), apply(lambda x: x[0], sequence(expression, satisfy(lambda x: x == ')'))))))
    # bind(apply(evaluate, sequence(value, times(sequence(satisfy(lambda x: x in '+-*/'), value)))))
    #
    # input_lines = get_input('day18.txt')
    # result = [x[0] for x in list(map(expression, input_lines))]
    #
    # print(sum(result))

    # part 2
    bind, expression = binding()
    value = choice(big_number, apply(lambda x: x[1], sequence(satisfy(lambda x: x == '('), apply(lambda x: x[0],
                                                                                                 sequence(expression,
                                                                                                          satisfy(lambda
                                                                                                                      x: x == ')'))))))
    add = apply(evaluate, sequence(value, times(sequence(satisfy(lambda x: x == '+'), value))))
    bind(apply(evaluate, sequence(add, times(sequence(satisfy(lambda x: x in '-*/'), add)))))

    input_lines = get_input('day18.txt')
    result2 = [x[0] for x in list(map(expression, input_lines))]

    print(sum(result2))


if __name__ == '__main__':
    main()

