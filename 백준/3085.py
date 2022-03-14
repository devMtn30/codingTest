N = int(input())
res = []
arr = []
for i in range(N):
    temp = []
    temp_str = input()
    for j in range(N):
        temp.append(temp_str[j])
    arr.append(temp)


def Candy(arr2):  # 사탕 개수 판별
    maxCandy = 1
    for i in range(N):
        tmp = arr2[i][0]  # 가로 첫번째
        tmpse = arr2[0][i]  # 세로 첫번쨰
        cnt = 1  # 가로 카운트
        cntse = 1  # 세로 카운트
        for j in range(1, N):
            # 가로 캔디 확인
            if tmp == arr2[i][j]:
                cnt += 1
            else:
                tmp = arr2[i][j]
                cnt = 1
            # 세로 캔디 확인
            if tmpse == arr[j][i]:
                cntse += 1
            else:
                tmpse = arr2[j][i]
                cntse = 1
            # 둘 중에 큰 값이랑 비교해서 큰값을 넣어주기
            if maxCandy < max(cnt, cntse):
                maxCandy = max(cnt, cntse)
    return maxCandy


for i in range(N):
    for j in range(N-1):
        arr[i][j + 1], arr[i][j] = arr[i][j], arr[i][j + 1]
        res.append(int(Candy(arr)))
        arr[i][j + 1], arr[i][j] = arr[i][j], arr[i][j + 1]
for i in range(N):
    for j in range(N-1):
        arr[j+1][i], arr[j][i] = arr[j][i], arr[j+1][i]
        res.append(int(Candy(arr)))
        arr[j+1][i], arr[j][i] = arr[j][i], arr[j+1][i]
print(max(res))
