# 문제
# 한 마을에 모험가가 N명 있습니다.
# 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
# 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
# 동빈이는 최대 몇개의 모험가 그룹을 만들 수 있는지 궁금합니다.
# 동빈이를 위해 N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
# 예를 들어 N=5이고, 각 모험가의 공포도가 다음과 같다고 가정합시다.
# 2 3 1 2 2
# 이때 그룹 1에 공포도가 1, 2, 3인 모험가를 한 명씩 넣고, 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면, 총 2개의 그룹을 만들 수 있습니다.
# 또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.

# 입력 조건
# 첫째 줄에 모험가의 수 N이 주어집니다. (1<=N<=100,000)
# 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

# 출력 조건
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

# 입력 예시 1
# 5
# 2 3 1 2 2

# 출력 예시 1
# 2

# 입력 예시 2
# 5
# 1 4 2 5 3

# 출력 예시 2
# 3

N = int(input())
group = sorted(list(map(int, input().split())))

print(group)
idx, answer = 0, 0
while True:
    nowValue = group[0]
    isUpdate = False

    if nowValue >= N:
        group.pop(0)
        answer += 1
        isUpdate = True

    for i in range(1, len(group) - 1):
        if group[i] + nowValue >= N:  # 현재 제일 작은 공포도를 가진 모험가가 여행을 떠날 수 있는지
            group.pop(i)
            group.pop(0)
            answer += 1
            isUpdate = True
            break

    if not isUpdate:
        popVal = group.pop(0)
        group[0] += popVal

    if sum(group) < N:
        break

print(answer)
