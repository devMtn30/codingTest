def bfs(graph, x, y):
    if x >= len(graph) or x < 0 or y >= len(graph[0]) or y < 0:
        return 0
    if graph[x][y] == 0:
        return 0
    if graph[x][y] > 0:
        graph[x][y] += -1

    bfs(graph, x + 1, y)
    bfs(graph, x - 1, y)
    bfs(graph, x, y + 1)
    bfs(graph, x, y - 1)

    return graph[x][y]


N = int(input())
result = []
for _ in range(N):
    temp = list(map(int, input().split()))
    result.append(temp)

cnt = 0
while True:
    cnt += 1
    doneFlag = True
    for i in range(N):
        for j in range(N):
            if bfs(result, i, j) != 0:
                doneFlag = False

    if doneFlag:
        break

print(cnt)