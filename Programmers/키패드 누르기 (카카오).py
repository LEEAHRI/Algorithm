numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

def solution(numbers, hand):
    answer = ''
    key_dict = {1: (0,0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left = [1, 4, 7]
    right = [3, 6, 9]
    left_hand = '*'
    right_hand = '#'

    for i in numbers:
        if i in left:
            answer += 'L'
            left_hand = i
        elif i in right:
            answer += 'R'
            right_hand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[left_hand]
            rPos = key_dict[right_hand]
            ldist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
            rdist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])

            if ldist < rdist:
                answer += 'L'
                left_hand = i
            elif ldist > rdist:
                answer += 'R'
                right_hand = i

            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = i
                else:
                    answer += 'R'
                    right_hand = i
    return answer

print(solution(numbers, hand))