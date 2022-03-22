N, M, V = map(int, input().split())


def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = []
graph.append([0])
visited = [False] * (N + 1)
for i in range(M):
    graph.append(list(map(int, input().split())))

dfs(graph, V, visited)
