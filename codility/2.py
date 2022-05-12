# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A = [1,3,2,5,6,4,7]

def solution(A):
    # write your code in Python 3.6
    ans = 0
    B = sorted(A)
    A_stack = []
    B_stack = []


    for n in range(len(A)):
        A_stack.append(A[n])
        B_stack.append(B[n])
        if sorted(A_stack) != B_stack:
            ans += 1
        else:
            continue
    return len(A) - ans

print(solution(A))