
        
        
def solution(numbers, target):
    def dfs(idx, sum):
        global answer
        if idx == len(numbers):
            if sum == target:
                return 1
            return 0

        a = dfs(idx+1, sum + numbers[idx])
        b = dfs(idx+1, sum - numbers[idx])
        
        return a+b
    
    answer = dfs(0,0)
    
    return answer