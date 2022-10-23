N = input()
people = list(map(int, input().split()))

temp = dict()
result = []
for i in people:
    temp[str(abs(i))] = 0

for i in people:
    cnt = 1
    if temp[str(abs(i))] == 1:
        cnt = 2
    temp[str(abs(i))] = cnt
for i in people:
    value = temp.get(str(abs(i)))
    if value == 1:
        result.append(i)

print(sum(result))