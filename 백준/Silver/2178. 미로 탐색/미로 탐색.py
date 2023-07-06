from collections import deque

N, M = map(int, input().split())

graph = [[0] * (M + 2) for _ in range(N + 2)]
visited = [[False] * (M + 2) for _ in range(N + 2)]

for i in range(N):
    temp = list(map(int, input()))
    for j in range(len(temp)):
        graph[i + 1][j + 1] = temp[j]
dirX = [1, -1, 0, 0]
dirY = [0, 0, 1, -1]
def bfs():
    global graph

    q = deque([(1, 1)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            newX = x + dirX[i]
            newY = y + dirY[i]
            if graph[newX][newY] == 1 and not visited[newX][newY]:
                graph[newX][newY] = graph[x][y] + 1
                q.append((newX, newY))
                visited[newX][newY] = True

bfs()
print(graph[N][M])
