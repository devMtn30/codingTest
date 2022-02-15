# 소수 구하기 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	148418	41635	29373	26.779%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def isPrime(number):
  for i in range(2,number):
    if number%i == 0:
      return False
  return True


import math
import sys

M,N =map(int,sys.stdin.readline().split())
Flag = [True] * (N+1)
num = int(math.sqrt(N))
for i in range(2,num+1):
  if Flag[i]:
    if isPrime(i):
      for j in range(i+i,N+1,i):
        Flag[j] = False

for i in range(M,N+1):
  if Flag[i] and i >= 2:
    print(i)



