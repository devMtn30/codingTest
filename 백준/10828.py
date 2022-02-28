from collections import deque
import sys

que = deque()
result = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
  num = 0
  command = ''

  tmp = sys.stdin.readline().rstrip()
  if tmp.find(" ") >= 0: #명령어랑 숫자가 주어지는지 판단
    command, num = tmp.split(" ")
  else:
    command = tmp
    
  if command == 'push':
    que.append(int(num))
  if command == 'top' and len(que) != 0:
    result.append(que[len(que)-1])
  elif command == 'pop' and len(que) != 0:
    result.append(que.pop())
  elif command == 'size' and len(que) != 0:
    result.append(len(que))
  elif command == 'size' and len(que) == 0:
    result.append('0')
  elif ((command == 'top' or command == 'pop') and len(que) == 0):
    result.append('-1')
    continue
  elif command == 'empty' :
    if len(que) > 0:
      result.append('0')
    else:
      result.append('1')

for i in result:
  print(i)

    