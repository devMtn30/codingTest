def solution(priorities, location):
    answer = 0
    while priorities:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            answer += 1
            if location == 0:
                return answer
        else:
            priorities.append(priorities.pop(0))
        location -= 1
        if location < 0:
            location = len(priorities) - 1