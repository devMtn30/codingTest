N = int(input())
xarr = [] #몸무게
yarr = [] #키
for i in range(N):
  x, y = map(int,input().split())
  xarr.append(x)
  yarr.append(y)

#순서 구하기
num1=xarr[0]
num2=yarr[0]
rank = [1] * N 
for i in range(N):
  num1 = xarr[i]
  num2 = yarr[i]
  for j in range(N):
    if num1 < xarr[j]:#몸무게가 더 크다면
      if num2 < yarr[j]:#키도 크다면
        rank[i]+=1
  
a = ""
for i in rank:
  a += str(i)+" "

print(a)