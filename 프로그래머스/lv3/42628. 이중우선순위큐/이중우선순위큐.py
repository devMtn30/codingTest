import heapq

def solution(operations):
    maxHeap = []
    minHeap = []
    for o in operations:
        current = o.split(" ")
        current[1] = int(current[1])
        if current[0] == "I":
            heapq.heappush(minHeap, current[1])
            heapq.heappush(maxHeap, (-current[1], current[1]))
        else: #삭제연산인 경우 
            if len(maxHeap) > 0 and current[1] == 1:
                heapq.heappop(maxHeap)
                if len(minHeap) > 0:
                    minHeap.pop()
            if len(minHeap) > 0 and current[1] == -1:
                heapq.heappop(minHeap)
                if len(maxHeap) > 0:
                    maxHeap.pop()
    maxVal = 0
    minVal = 0
    if len(maxHeap) > 0:
        maxVal = heapq.heappop(maxHeap)
        maxVal = maxVal[1]
    if len(minHeap) > 0:
        minVal = heapq.heappop(minHeap)
    
    return [maxVal, minVal]