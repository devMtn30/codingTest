from collections import Counter

N, M = map(int, input().split())

resultDict = dict()
#1:1 2:1 3:1 4:1
#1:2 2:1 3:1
for _ in range(M):
    temp = list(map(int, input().split()))
    tempDict = {item: 0 for item in temp[1:]}
    for item in temp[1:]:
        tempDict[item] += 1
    resultDict = dict(Counter(tempDict) + Counter(resultDict))

result = []
maxVal = 0

for key, val in resultDict.items():
    if val >= maxVal:
        maxVal = val
        result.append(key)
    # 이미 저장된 값보다 현재값이 더 크다면 리스트를 비운 뒤 현재 값 추가
    if resultDict[result[0]] < val:
        result.clear()
        result.append(key)
print(*sorted(result, reverse=True))

