N = int(input())

strList = []
for i in range(N):
    inputStrList = input().split(" ")

    tempList = []
    for inputStr in inputStrList:
        tempList.append(inputStr[::-1])
    strList.append(" ".join(tempList))

for str in strList:
    print(str)

