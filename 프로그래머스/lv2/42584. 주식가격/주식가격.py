def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        #print(prices[i])
        for j in range(i,len(prices)-1):
            #print(prices[j])
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break
        #print("========")
    return answer