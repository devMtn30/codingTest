# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

import sys

result = []
N = int(sys.stdin.readline().rstrip())
arrA = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(input())
arrM = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return 0
    # 중간점 찾기
    mid = (start + end) // 2
    # 데이터를 찾은 경우
    if arr[mid] == target:
        return 1
    # 중간점보다 왼쪽에 데이터가 있는 경우
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    # 중간점보다 오른쪽에 데이터가 있는 경우
    else:
        return binary_search(arr, target, mid + 1, end)


for i in arrM:
    print(binary_search(arrA, i, 0, len(arrA) - 1))
