#1칠하는 알고리즘 만들기
#2.N을 한번 쭉 훑고 M을 1씩 증가시키면서 반복
#3.몇번 칠해야하는지 cnt를 append
#4.최소값 출력
import sys
N,M = map(int,sys.stdin.readline().split())

arr = []
result = []
for _ in range(N):
  arr.append(sys.stdin.readline().rstrip())

for i in range(N-7):
  for j in range(M-7):
    idx1 = 0
    idx2 = 0
    for k in range(i,i+8):
      for l in range(j,j+8):
        if (k+l) % 2 == 0:
          if arr[k][l] != 'W':
            idx1 +=1
          if arr[k][l] != 'B':
            idx2 +=1
        else:
          if arr[k][l] != 'B':
            idx1 +=1
          if arr[k][l] != 'W':
            idx2 +=1
    result.append(min(idx1,idx2))
          

print(min(result))

