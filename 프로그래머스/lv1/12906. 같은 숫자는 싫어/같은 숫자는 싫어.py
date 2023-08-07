def solution(arr):
    answer = []
    beforeNum = -1
    for item in arr:
        if beforeNum != item:
            answer.append(item)
        beforeNum = item
    return answer