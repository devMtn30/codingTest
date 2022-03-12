arr = list(map(int,input().split()))
arr.sort()
res = ''
for i in range(3):
    if arr == 2:
        res += str(arr[i])
    else:
        res += str(arr[i])+" "
print(res)
