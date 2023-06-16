def dfs(idx):
    global visit
    visit[idx] = True
    print(idx, end = ' ')
    
    for next in range(1, N+1):
        if graph[idx][next] and not visit[next]:
            dfs(next) 
            
def bfs(idx):
    global q, visit
    
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N+1):
            if graph[cur][next] and not visit[next]:
                visit[next] = True
                q.append(next)

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visit = [False] * (N + 1)

#방문처리
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

    
dfs(V)
print()

visit = [False] * (N + 1)
q = [V]
visit[V] = True
bfs(V)