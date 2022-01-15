#한 마을에 모험가가 N명이 있다. 모험가는 각자 공포도 X가 있으며 공포도가 X인 모험가는 반드시 X명이상으로 구성된 모험가 그룹에 참여해야 여행을 떠날수있다.
#최대 몇개의 모험가 그룹을 만들 수 있는지?
#여행을 떠날 수 있는 그룹의 최댓값을 구하는 프로그램


#예를 들어 N=5이고 각 모험가의 공포도가 다음과 같다고 가정
#2 3 1 2 2

#이 경우 그룹 1에 공포도가 1,2,3인 모험가를 한명씩 넣고
#그룹 2에 공포도가 2인 남은 두명을 넣어서 총 2개의 그룹을 만들수있다.

#즉 자신의 공포도 이상의 인원이 있어야 여행이 가능. 또한 모든 모험가는 여행에 나서지 않아도 괜찮다.

#입력조건 : 첫째줄에 모험가의 수 N이 주어진다 (1이상, 10만이하)
#둘째줄에 각 모험가의 공포도 값을 N이하의 자연수로 주어지며 각 자연수는 공백으로 구분

#출력조건 : 여행을 떠날 수 있는 그룹 수의 최댓값을 출력

import sys
#1.모험가의 수를 입력받는다.
leaveTeam = 0
leaveCnt = 1
n = int(input())
#2.각 모험가의 수 만큼 공포도를 입력받는다. 공백을 기준
x = input().split(" ")
#3.낮은수부터 정렬
x.sort()
#4.수에 해당하는 만큼 여행시키기(제외)

#만약 6명이고 1 1 1 2 2 2
for i in range(0,n):
  #공포도랑 팀 길이 비교
  if int(x[i]) == leaveCnt :
    #6.여행 시킨 팀 추가
    leaveTeam +=1
    leaveCnt = 1 
  else :
    leaveCnt+=1

print(leaveTeam)