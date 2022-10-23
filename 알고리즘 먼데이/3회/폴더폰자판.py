# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
S = list(input())

num = [['1', '.', '?', '!'],
       ['2', 'A', 'B', 'C'],
       ['3', 'D', 'E', 'F'],
       ['4', 'G', 'H', 'I'],
       ['5', 'J', 'K', 'L'],
       ['6', 'M', 'N', 'O'],
       ['7', 'P', 'Q', 'R', 'S'],
       ['8', 'T', 'U', 'V'],
       ['9', 'W', 'Y', 'Z']]

temp = S[0]
cnt = 0
for i in range(1, len(S)):
    if temp != S[i]:
        # 만약 이전이랑 다르면 문자 출력
        number = S[i]
        ream = 4
        if S[i] == '1' or S[i] == '7' or S[i] == '9':
            ream = 4
        cnt = cnt % ream
        print(num[int(number) - 1][cnt])
        cnt = 0
    cnt += 1
    temp = S[i]

# 14
# 44433355556666
