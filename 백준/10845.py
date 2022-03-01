from collections import deque
import sys

que = deque()
def push(X):
  que.append(X)
def pop():
  if len(que) == 0:
    return -1
  return que.popleft()
def size():
  return len(que)
def empty():
  if len(que) == 0:
    return 1
  return 0
def front():
  if len(que) == 0:
    return -1
  return que[0]
def back():
  if len(que) == 0:
    return -1
  return que[-1]

result = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
  tmp = sys.stdin.readline().rstrip()

  if tmp.find('push') >= 0:
    command, num = tmp.split()
    push(int(num))
  elif tmp.find('pop') >= 0:
    result.append(pop())
  elif tmp.find('size') >= 0:
    result.append(size())
  elif tmp.find('empty') >= 0:
    result.append(empty())
  elif tmp.find('front') >= 0:
    result.append(front())
  elif tmp.find('back') >= 0:
    result.append(back())
for i in result:
  print(i)
