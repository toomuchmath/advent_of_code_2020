from functools import reduce


def get_input(filename):

    with open(filename) as f:
        lines = f.read().split('\n\n')

    return lines


def distinct_questions(questions):

    questions_set = set(questions)
    questions_set.discard('\n')

    return ''.join(questions_set)


def count_questions(distinct_questions_list):

    return len(distinct_questions_list)


def common_questions(questions):

    split_questions = questions.split('\n')

    def common(q1, q2):
        return set(q1) & set(q2)

    result = reduce(common, split_questions)

    return len(result)


def main():
    input_list = get_input('day06.txt')
    # questions_list = list(map(distinct_questions, input_list))
    # print(questions_list)
    # questions_count = list(map(count_questions, questions_list))
    # print(questions_count)
    # total_count = sum(questions_count)
    # print(total_count)
    questions_list = list(map(common_questions, input_list))
    print(sum(questions_list))


if __name__ == '__main__':
    main()
