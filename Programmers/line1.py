logs = ["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]
# 0 1 2 3 4 5 6 7 8 9 10 11
# result = ' '.join(s for s in set(logs))
# new_list = result.split()
# print(new_list)
# # print(set(logs))
# print(new_list[3])

# problem_dict = {
#     'reverse': 0,
#     'string_compare': 0,
#     'sort': 0,
#     'sqrt': 0
# }
#
# def solution(logs):
#     a = []
#     b = []
#     for log in logs:
#         first, second = log.split()
#         a.append(first)
#         b.append(second)
#     for n in range(len(a)):
#         print(a[n], b[n])


def solution(logs):
    logs = set(logs)
    person_set = set()
    problem_dict = {}
    for log in logs:
        person, problem = log.split()
        person_set.add(person)
        if problem not in problem_dict:
            problem_dict[problem] = 1
        else:
            problem_dict[problem] = problem_dict[problem] + 1

    answer = []
    people_count = len(person_set)
    for problem in problem_dict.keys():
        if problem_dict[problem] >= people_count / 2:
            answer.append(problem)
    return sorted(answer)



# print(solution(logs))
print(solution2(logs))