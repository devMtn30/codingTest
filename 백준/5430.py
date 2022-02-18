import sys
T = int(sys.stdin.readline().strip())
result = []

for i in range(T):
  p = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline().strip())
  arr = sys.stdin.readline().strip()

  if arr == '[]' and p.count('D') >= 1:
    print('error')
    continue
  if arr == '[]':
    result.append('[]')
    continue
    
  front = 0
  back = 0
  flag = True
  for j in p:
    if j == 'R':
      if flag:
        flag = False
      else:
        flag = True
    if flag:
      if j == 'D':
        back+=1
    else:
      if j == 'D':
        front+=1
  
 
  arr = list(map(int,arr[1:-1].split(',')))
  
  if p.count('R') % 2 == 1: 
    arr.reverse()
  if n-p.count('D') < 0:
    result.append('error')
  else:
    result.append(arr[front:-back])
for i in result:
  temp = ''.join(str(i))
  temp = temp.replace(' ','')
  print(temp+"결과")

