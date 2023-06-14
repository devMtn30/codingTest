N = int(input())
score_list = list(map(int,input().split()))

total_score = 0
bonus_score = 0
for score in score_list:
    if score == 1:
        bonus_score +=1
        total_score += bonus_score
    else:
        bonus_score = 0
print(total_score)
    