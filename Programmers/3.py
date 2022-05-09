def solution(init_alp, init_cop, problems):
    target_alp, target_cop = init_alp, init_cop
    for problem in problems:
        target_alp = target_alp if target_alp > problem[0] else problem[0]
        target_cop = target_cop if target_cop > problem[1] else problem[1]

    power_board = [[0 for _ in range(target_cop + 1)] for _ in range(target_alp + 1)]
    for alp in range(init_alp, target_alp + 1):
        for cop in range(init_cop, target_cop + 1):
            power_board[alp][cop] = (alp - init_alp) + (cop - init_cop)
            for problem in problems:
                prev_alp = init_alp if init_alp > alp - problem[2] else alp - problem[2]
                prev_cop = init_cop if init_cop > cop - problem[3] else cop - problem[3]
                if problem[0] > prev_alp or problem[1] > prev_cop:
                    continue
                candidate = power_board[prev_alp][prev_cop] + problem[4]
                if power_board[alp][cop] > candidate:
                    power_board[alp][cop] = candidate

    for row in power_board:
        print(row)

    return power_board[target_alp][target_cop]


sol = solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]])
# sol = solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])
print(sol)