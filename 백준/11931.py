import sys
N = int(input())
arr = []
for i in range(N):
  arr.append(int(sys.stdin.readline()))

arr = sorted(arr,reverse=True)

for i in arr:
  print(i)