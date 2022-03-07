import sys


primeNum = [True] * 10001
primeNum[1] = False
# 소수 구하기
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        primeNum[j] = False
# 입력 받기
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    for j in range(a//2, 0, -1):
        if primeNum[j] and primeNum[a - j]:
            print(j, a - j)
            break
