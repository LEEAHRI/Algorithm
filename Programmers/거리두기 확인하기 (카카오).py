from collections import deque
def dfs(place, row, col):
    dx = [1, -1, 0, 0] #동서남북
    dy = [0, 0, 1, -1]
    visited = [[0] * 5 for _ in range(5)]
    Q = deque()
    Q.append((row,col,0))

    while Q:
        curr = Q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x <= 4 and 0 <= y <= 4 and places[x][y] == P:
                dis[x]




def solution(places):
    answer = []
    return answer

