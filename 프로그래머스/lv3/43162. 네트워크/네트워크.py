import sys

def solution(n, computers):
    sys.setrecursionlimit(10**7)
    answer = 0
    
    visited = [False] * n
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
               dfs(j)
        
    for computer in computers:
        for i in range(n):
            if computer[i] == 1 and not visited[i]:
                dfs(i)
                answer+=1
    
    
    return answer