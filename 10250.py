import math

T = int(input())


#데이터 입력받기
result = []
for i in range(T):
  H,W,N = map(int,input().split())
  rm = math.ceil(N//H)+1
  floor = N%H

  #if floor == 0:
    
  if rm >=10:
    result.append(str(floor)+str(rm))
  else:
    result.append(str(floor)+'0'+str(rm))

for res in result:
  print(res)