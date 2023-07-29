def solution(clothes):
    dic = {}
    for clothe in clothes:
        if clothe[1] in dic.keys():
            dic[clothe[1]].append(clothe[0])
        else:
            dic[clothe[1]] = [clothe[0]]
    
    answer = 1
    for value in dic.values():
        answer *= len(value) + 1
    return answer - 1