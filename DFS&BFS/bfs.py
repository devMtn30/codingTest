#bfs 구현 복습
from collections import deque

def bfs(graph,visit,startnode):
  queue = deque([startnode])
  visit[startnode] = True

  while queue:
    v = queue.popleft()
    print(v,end=' ')
    
    for i in graph[v]:
      if not (visit[i]):
        queue.append(i)
        visit[i]= True


graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visit = [False]*9

bfs(graph,visit,1)