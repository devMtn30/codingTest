def solution(numbers, target):
    def dfs(sum, i):
        if i == len(numbers):
            if sum == target:
                return 1
            else:
                return 0

        return dfs(sum + numbers[i], i+1) + dfs(sum - numbers[i], i+1) 
    return dfs(0,0)
