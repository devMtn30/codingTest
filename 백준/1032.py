N = int(input())
arr = []
for i in range(N):
    arr.append(input())

before = arr[0]
result = []
for i in arr:
    for j in range(len(i)):
        if before[j] != i[j]:
            result.append(int(j))

a = ''

for i in range(len(before)):
    if i in result:
        a += '?'
    else:
        a += before[i]

print(a)
