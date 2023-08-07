N = int(input())

ans = []
for _ in range(N):
    dice = sorted(list(map(int,input().split())))
    dset = set(dice)
    
    if len(dset) == 1:
        ans.append(50000+dice[0]*5000)
    if len(dset) == 2:
        if dice[1] == dice[2]:
            ans.append(10000+dice[1]*1000)
        else:
            ans.append(2000+(dice[1]*500)+(dice[2]*500))
    else:
        flag = True
        for i in range(3):
            if dice[i] == dice[i+1]:
                flag = False
                ans.append(1000+dice[i]*100)
        if flag:
            ans.append(max(dice)*100)

print(max(ans))