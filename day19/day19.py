def get_input(filename):
    with open(filename) as f:
        rules, strings = f.read().split('\n\n')
    return rules, strings


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


def sequences(parser, *parsers):
    result = apply(lambda x: [x], parser)
    for p in parsers:
        result = apply(lambda x: x[0] + [x[1]], sequence(result, p))
    return apply(lambda x: tuple(x), result)


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


def question(parser):
    def h(string):
        result = parser(string)
        if result is not None:
            return result
        return None, string
    return h


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


def right(parser):
    return apply(lambda x: x[1], parser)


def binding():
    x = [lambda x: x]

    def bind(y):
        x[0] = y

    def parser(string):
        return x[0](string)

    return bind, parser


def main():
    # rules, strings = get_input('day19.txt')
    rules = """0: 1 2
    1: "a"
    2: 1 3 | 3 1
    3: "b"
    """

    """
    Bottom      ← [ab]+

    Number      ← [0-9]+
    Rule        ← '"' [ab] '"' / (Number ' ' Number (' | ' Number ' ' Number)?)
    Top         ← Number ': ' Rule 
    File        ← Top ('\n' Top)+ '\n\n' Bottom ('\n' Bottom)+
    """

    ab = satisfy(lambda x: x in 'ab')
    bottom = plus(ab)

    number = apply(lambda x: int(''.join(x)), plus(satisfy(lambda n: n in '0123456789')))
    space = satisfy(lambda s: s == ' ')
    numbers = apply(lambda x: [x[0]] + x[1], sequence(number, plus(right(sequence(space, number)))))
    quote = satisfy(lambda q: q == '"')
    pipe = sequences(space, satisfy(lambda p: p == '|'), space)
    rule = choice(apply(lambda x: x[1], sequences(quote, ab, quote)), sequences(numbers, question(right(sequence(pipe, numbers)))))
    colon = sequence(satisfy(lambda c: c == ':'), space)
    top = apply(lambda x: (x[0], x[2]), sequences(number, colon, rule))
    new_line = satisfy(lambda n: n == '\n')
    file = apply(lambda x: (x[0], x[1], x[4], x[5]), sequences(top, plus(right(sequence(new_line, top))), new_line, new_line, bottom, plus(right(sequence(new_line, bottom)))))

    print(top('0: 1 2'))
    print(bottom('ababababa'))
    print(rule('1 3 | 3 1'))

    with open('day19.txt') as f:
        txt = f.read()
    print(file(txt))


if __name__ == '__main__':
    main()