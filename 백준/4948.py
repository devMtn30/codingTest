import math

result = []
N = 1234567
arr = [True] * (N+1)
for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i]:
        j = 2
        while i * j <= N:
            arr[i * j] = False
            j += 1
while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in range(N+1, N*2+1):
        if arr[i]:
            cnt += 1
    result.append(cnt)

for i in result:
    print(i)
