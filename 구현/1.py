#시뮬레이션,완전탐색 문제유형

#여행가 A는 N * N 크기의 정사각형위에 서있다. 가장 왼쪽 위 좌표부터 시작하며 (1,1)이다.
#여행가 A에게는 이동 계획서가 있는데
#계획서에 하나의 줄에 띄어쓰기를 기준으로 LRUD중 하나의 문자가 반복적으로 적혀있다.
#L : 왼쪽 , R : 오른쪽 , U : 위쪽 , D : 아래쪽
#이때 여행가 A는 정사각형의 공간을 벗어나는 움직임은 무시한다.

#입력 조건 : 첫째 줄에는 공간의 크기를 나타내는 N이 주어진다. 1이상 100이하
#둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. 1이상 100이하

#출력조건 : 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백을 기준으로 구분하여 출력
import time

# 프로그램 소스코드
#공간의 크기 입력 받기
areaSize = int(input())

#계획서 입력받기
plan = input().split(" ")

#공간 생성
import numpy
x,y = 0,0

start_time = time.time() # 측정 시작


for i in plan:
  if not x== -1 or not x > areaSize or not y == -1 or not y > areaSize:
    if i == "L" and y > 0 :
      y-=1
    elif i == "R" and y < areaSize:
      y+=1
    elif i == "D" and x < areaSize:
      x+=1
    elif i == "U" and x > 0:
      print("up")
      x-=1

x+=1
y+=1


print(x,y)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력


