N = int(input())

result = []
for i in range(N):
    tempList = list(input())
    cnt = 0
    flag = False
    for temp in tempList:
        if temp == "(":
            cnt+=1
        if temp == ")":
            cnt-=1
        if cnt < 0:
            flag = True
    if cnt != 0 or flag:
        result.append("NO")
    else:
        result.append("YES")

for res in result:
    print(res)