# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A = 53
B = 153786
def solution(A, B):
    # write your code in Python 3.6


    list_A = list(map(int, str(A)))
    list_B = list(map(int, str(B)))
    list_total = list_A+list_B

    #한 자리면 해당 인덱스 반환
    if len(list_A) == 1:
        for k in range(len(list_B)):
            if list_B[k] == list_A[0]:
                return k

    #요소의 순서와 상관 없이 가지고만 있더라도.
    if len(list(set(list_total)) == len(list_B):
        for i in range(len(list_B)-1):

    else:
        return -1





                for j in range(len(stack)-1):
                    for m in range(len(list_A)-1):
                        if (list_B[j] != list_A[m]) and (list_B[j+1] != list_A[m+1]):
                            return j
                        else:
                            return -1














print(solution(A, B))









