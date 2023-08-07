import sys

sys.setrecursionlimit(10 ** 6)

dirR = [0, 0, 1, -1]
dirC = [1, -1, 0, 0]


def dfs(x, y):
    global aptCnt, visited
    visited[x][y] = True
    aptCnt += 1
    for i in range(4):
        newX = x + dirR[i]
        newY = y + dirC[i]
        if graph[newX][newY] and not visited[newX][newY]:
            dfs(newX, newY)


N = int(input())

graph = [[False] * (27) for _ in range(27)]
visited = [[False] * (27) for _ in range(27)]
for i in range(N):
    temp = list(map(int,input().rstrip()))
    for j in range(len(temp)):
        if temp[j] == 1:
            graph[i+1][j+1] = True
            
ansList = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] and not visited[i][j]:
            aptCnt = 0
            dfs(i, j)
            ansList.append(aptCnt)

print(len(ansList))
for ans in sorted(ansList):
    print(ans)
