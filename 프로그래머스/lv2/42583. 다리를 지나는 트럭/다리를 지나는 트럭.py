def solution(bridge_length, weight, trucks):
    que = [0 for _ in range(bridge_length)]      
    answer = 0
    now_weight = 0
    while que:
        now_weight -= que.pop(0)
        answer+=1
        
        if trucks:
            if now_weight + trucks[0] <= weight:
                temp = trucks.pop(0)
                now_weight += temp
                que.append(temp)
            else:
                que.append(0)
    return answer