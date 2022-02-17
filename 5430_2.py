import sys
from collections import deque
import re
T = int(sys.stdin.readline().strip())
result = []
 

queue = deque()
for i in range(T):
  flag=True
  p = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline().strip())
  arr = sys.stdin.readline().strip()
  arr = arr[1:-1]
  arr = arr.split(',')
  for i in arr:
    queue.append(int(i))
  cnt = 0
  for method in p:
    if method == 'R':
      if flag:
        flag=False
      else:
        flag=True
    if method == 'D':
      if n != 0:
        n-=1
        if flag:#리버스 안됐으면 오른쪽 제거
          queue.pop()
        else:#리버스면 왼쪽제거
          queue.popleft()
      else:
        print.append('error')
        break
    cnt+=1
    if cnt == len(p):
      print(queue)
      for i in queue:
        print(i)
        result.append(i)
      print(result)
  if flag: #삭제되었으면 append flag 안해주면 비어있는 arr [] 추가됨
    print(result)
  else:
    print(result.reverse())

