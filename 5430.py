import sys
T = int(sys.stdin.readline().strip())
result = []

for i in range(T):
  reversecnt = 0
  flag = True
  p = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline().strip())
  arr = sys.stdin.readline().strip()
  arr = arr[1:-1]
  arr = list(map(int,arr.split(',')))
  for method in p:
    if method == 'R':
      reversecnt+=1
  if reversecnt % 2 == 1: 
    arr.reverse()
  for method in p:
    if method == 'D':
      if n != 0:
        n-=1
        del arr[0]
      else:
        result.append('error')
        flag=False
        break;
  if flag:
    result.append(arr)
for i in result:
  print(i)

