from collections import deque

q= deque(map(int,input().split()))
arr = []
print(max(q))
for i in q:
  arr.append(min(q))
  q.remove(min(q))
print(arr)