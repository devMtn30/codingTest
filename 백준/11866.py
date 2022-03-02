N, K = map(int,input().split())
arr = [i for i in range(1,N+1)]
result = []
tmp = 0

for i in range(1,N+1):
  tmp += K-1
  if tmp >= len(arr):
    tmp = tmp % len(arr)
    
  result.append(arr.pop(tmp))


print('<',end='')
print(', '.join(map(str,result)),end='')
print('>')