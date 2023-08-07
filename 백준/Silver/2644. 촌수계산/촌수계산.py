def dfs(startNode):
    for i in graph[startNode]:
        if visited[i] == -1:
            visited[i] = visited[startNode] + 1
            dfs(i)

N = int(input())

a, b = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1 for _ in range(N + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited[a] = 0
dfs(a)
print(visited[b])