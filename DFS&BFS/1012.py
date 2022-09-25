import sys

sys.setrecursionlimit(10 ** 6)
T = int(input())


def dfs(x, y, matrix):
    if x < 0 or y < 0:
        return False
    if len(matrix) <= x or len(matrix[0]) <= y:
        return False
    if matrix[x][y] != 1:
        return False

    matrix[x][y] = 0  # 방문처리
    dfs(x + 1, y, matrix)
    dfs(x - 1, y, matrix)
    dfs(x, y + 1, matrix)
    dfs(x, y - 1, matrix)

    return True

for i in range(T):
    M, N, K = list(map(int, input().split()))
    matrix = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                dfs(i, j, matrix)
                cnt += 1
    print(cnt)
