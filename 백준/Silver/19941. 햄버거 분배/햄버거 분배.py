# https://www.acmicpc.net/problem/19941

N, K = map(int, input().split())
arr = list(input())
rangeList = []
for i in range(-K,K+1): #먹을 수 있는 범위 (음수부터)
    rangeList.append(i)

for i in range(N):
    if arr[i] == "P":
        for j in rangeList:
            now = i+j
            if 0 <= now < N and arr[now] == "H":
                arr[now] = "E" #Eat
                break

answer = 0
for i in arr:
    if i == "E":
        answer+=1
print(answer)