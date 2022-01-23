# 미로탈출 : 문제 조건
# 첫째줄에 두 정수 N,M이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어집니다. 각각의 수들ㅇ느 공백없이 붙어서 입력으로 제시 또한 시작과 마지막칸은 항상 1입니다.

# 출력조건 : 첫째 줄에 최소 이동칸의 개수를 출력합니다.
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력예시 : 10 
from collections import deque

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny <0 or ny >=m:
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] ==1:
        graph[nx][ny] = graph[x][y] +1
        queue.append((nx,ny))

  return graph[n-1][m-1]

n,m map(int,input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

#day11