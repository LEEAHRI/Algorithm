import grade as grade

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]


# survey =[]
# choices = []
# print(sorted(survey))

# survey = ["TR", "RT", "TR"]
# choices = [7, 1, 3]


type_order_dict = {1: ['R', 'T'],
             2: ['C', 'F'],
             3: ['J', 'M'],
             4: ['A', 'N']}

type_dict = {'R': 0, 'T': 0,
             'C': 0, 'F': 0,
             'J': 0, 'M': 0,
             'A': 0, 'N': 0}



# print(type_dict[1][0])


def solution(survey, choices):
    #survey가 없는 경우
    if len(survey) == 0:
        return 'RCJA'




    for idx in range(len(survey)):
        if survey[idx] == "RT":
            if choices[idx] >= 5:
                type_dict['T'] += (choices[idx]-4)
            else:
                type_dict['R'] += (4-choices[idx])
        if survey[idx] == "TR":
            if choices[idx] >= 5:
                type_dict['R'] += (choices[idx]-4)
            else:
                type_dict['T'] += (4-choices[idx])
        if survey[idx] == "CF":
            if choices[idx] >= 5:
                type_dict['F'] += (choices[idx]-4)
            else:
                type_dict['C'] += (4-choices[idx])
        if survey[idx] == "FC":
            if choices[idx] >= 5:
                type_dict['C'] += (choices[idx]-4)
            else:
                type_dict['F'] += (4-choices[idx])
        if survey[idx] == "JM":
            if choices[idx] >= 5:
                type_dict['M'] += (choices[idx]-4)
            else:
                type_dict['J'] += (4-choices[idx])
        if survey[idx] == "MJ":
            if choices[idx] >= 5:
                type_dict['J'] += (choices[idx]-4)
            else:
                type_dict['M'] += (4-choices[idx])
        if survey[idx] == "AN":
            if choices[idx] >= 5:
                type_dict['N'] += (choices[idx]-4)
            else:
                type_dict['A'] += (4-choices[idx])
        if survey[idx] == "NA":
            if choices[idx] >= 5:
                type_dict['A'] += (choices[idx]-4)
            else:
                type_dict['N'] += (4-choices[idx])

    answer = ''
    for key, value in type_order_dict.items():
        item1_weight = type_dict[value[0]]
        item2_weight = type_dict[value[1]]
        if item1_weight == item2_weight:
            answer += value[0]
        elif item1_weight < item2_weight:
            answer += value[1]
        else:
            answer += value[0]


    return answer

#
# #
# #     # answer = ''
# #     # for key, value in type_dict.items():
# #     #     flag = False
# #     #     for ch in value:
# #     #         if ch in a:
# #     #             answer += ch
# #     #             flag = True
# #     #             break
# #     #     if not flag:
# #     #         answer += value[0]
# #     #
# #     # return answer
# #
print(solution(survey, choices))
