#1칠하는 알고리즘 만들기
#2.N을 한번 쭉 훑고 M을 1씩 증가시키면서 반복
#3.몇번 칠해야하는지 cnt를 append
#4.최소값 출력
import sys
N,M = map(int,sys.stdin.readline().split())

arr = []
for i in range(N):
  arr.append(sys.stdin.readline())


