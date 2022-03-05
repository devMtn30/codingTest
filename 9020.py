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
    numArr2 = []
    for j in range(int(x/2)):#첫번째 소수를 구하고, 두번째 소수는 첫번째 소수의 큰것부터 작은것까지 넣어서 비교해본다.
        if flag:
            break
        numArr2.append(numArr[j])
        for k in reversed(numArr2):
            if k+k == x:
                primeNum1 = k
                primeNum2 = k
                flag = True
                break
            if numArr[j] + k == x:
                primeNum1 = k
                primeNum2 = numArr[j]
                flag = True
                break
    print(primeNum1, primeNum2)