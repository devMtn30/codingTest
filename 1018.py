#1칠하는 알고리즘 만들기
#2.N을 한번 쭉 훑고 M을 1씩 증가시키면서 반복
#3.몇번 칠해야하는지 cnt를 append
#4.최소값 출력
import sys
N,M = map(int,sys.stdin.readline().split())

arr = []
result = []
for i in range(N):
  arr.append(sys.stdin.readline().rstrip())
print("------------")
for i in range(N): #배열 전체
  if i+7 >= N:
    break
  tempN = arr[i:i+8]#0~8줄
  for j in range(M):#옆으로 한칸씩
    if j+7 >= M:
      break
    tempM = tempN[j:j+8]
    cnt = 0    
    for k in tempM:#한줄씩
      pre = tempM
      print(tempM)
      for l in k: #한문장씩 비교
        if pre == l:
          print(k[0][0])
          cnt+=1
        pre = l
    result.append(cnt)
    print(cnt)

print(min(result))