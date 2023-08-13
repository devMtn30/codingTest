arr = input()
target = input()
tlen = len(target)
cnt = 0

i = 0
while len(arr) - tlen >= i:
    if arr[i:i + tlen] == target:
        cnt += 1
        i = i + tlen
    else:
        i+=1

print(cnt)
