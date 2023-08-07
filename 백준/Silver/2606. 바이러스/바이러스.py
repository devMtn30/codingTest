def dfs(v):
    #동작
    visited[v] = True
    for next in range(1, N + 1):
        if not visited[next] and graph[v][next]:
            dfs(next)

N = int(input())
M = int(input())

graph = [[False] * (N+1) for _ in range(N + 1)]
visited = [False] * (N+1)

#노드 방문처리
for i in range(M):
    x, y = map(int,input().split())
    graph[x][y] = True
    graph[y][x] = True

dfs(1)
total = 0
for i in visited:
    if i:
        total+=1
print(total-1)