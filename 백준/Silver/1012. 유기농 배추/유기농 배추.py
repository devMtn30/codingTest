import sys
sys.setrecursionlimit(10**6)

colY = [1, -1, 0, 0]
colX = [0, 0, 1, -1]


def dfs(x, y):
    global visited
    visited[x][y] = True

    for i in range(4):
        newX = x + colX[i]
        newY = y + colY[i]
        if graph[newX][newY] and not visited[newX][newY]:
            dfs(newX, newY)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[False] * 60 for _ in range(60)]
    visited = [[False] * 60 for _ in range(60)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x + 1][y + 1] = True

    answer = 0
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)