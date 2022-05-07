import re, itertools, copy


def calculate(cal, number_a, number_b):
    if cal == '-':
        return number_a - number_b
    if cal == '+':
        return number_a + number_b
    if cal == '*':
        return number_a * number_b


def solution(expression):
    numbers = re.findall(r'\d+', expression)
    cal = re.findall(r'\W', expression)

    list_expressions = [int(numbers[0])]
    for idx in range(len(cal)):
        list_expressions.append(cal[idx])
        list_expressions.append(int(numbers[idx + 1]))

    cals = ['+', '*', '-']
    cals_priorities = itertools.permutations(cals)
    answer = -1
    for priority in cals_priorities:
        copied_list_expressions = copy.deepcopy(list_expressions)

        for cal in priority:
            for idx, item in enumerate(copied_list_expressions):
                if item == cal:
                    left_idx, right_idx = idx - 1, idx + 1
                    while copied_list_expressions[left_idx] is None:
                        left_idx -= 1
                    while copied_list_expressions[right_idx] is None:
                        right_idx += 1

                    new_number = calculate(cal, copied_list_expressions[left_idx], copied_list_expressions[right_idx])
                    copied_list_expressions[left_idx] = new_number
                    copied_list_expressions[idx] = None
                    copied_list_expressions[right_idx] = None

        answer = max(answer, abs(copied_list_expressions[0]))

    return answer
