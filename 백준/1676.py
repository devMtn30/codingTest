import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0

while N >= 5:
    cnt += N // 5
    N //= 5

print(int(cnt))