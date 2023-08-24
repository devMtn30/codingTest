N = int(input())
target = list(input())
cnt = 0

bColor = target[0]
cnt = 0
before = bColor
for now in target:
    # 만약 처음 고른 컬러와 현재가 다르면서, 이전 컬러와 다른 색인 경우 cnt+1
    cnt = cnt+1 if now != bColor and now != before else cnt
    before = now

print(cnt + 1)