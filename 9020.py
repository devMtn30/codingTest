import sys
import math

numArr = []
primeNum = [True] * 10001
# 소수 구하기
for i in range(2, 10001):  # sqrt +1까지만 루프 돌면 됨
    if primeNum[i]:
        numArr.append(i)
        j = 2
        while i * j <= 10000:  # 에라토스테네스의 체 구현
            primeNum[i * j] = False
            j += 1

# 입력 받기
primeNum1 = 2
primeNum2 = 2
arr = []

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
# 골드바흐 파티션 구하기
for x in arr:
    flag = False
    for j in numArr:
        if flag:
            break
        for k in numArr:
            if k+k == x:
                primeNum1 = k
                primeNum2 = k
                flag = True
                break
            if j + k == x:
                primeNum1 = j
                primeNum2 = k
                flag = True
                break
    print(primeNum1, primeNum2)
