N = int(input())

result = []
stack = []
cnt = 1
minusFlag = False
for _ in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        result.append("+")
        cnt+=1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        minusFlag = True
        break

if not minusFlag:
    for i in result:
        print(i)