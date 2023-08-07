import heapq

def solution(jobs):
    total, start, end, cnt = 0, -1, 0, 0
    heap = []
    
    while len(jobs) > cnt:
        for job in jobs: #현재 작업이 끝나자마자 실행 가능성이 있는 작업만
            if start < job[0] <= end:
                heapq.heappush(heap, [job[1], job[0]])
        #1.짧게 대기하는 작업을 꺼내오기
        if len(heap) > 0:
            job = heapq.heappop(heap)
            print(job)
            start = end
            end += job[0]
            total += end - job[1]
            cnt += 1
            #print("start="+str(start)+" end="+str(end)+" total="+str(total))
        else:
            end+=1
        
    return int(total / len(jobs))