def fibo(n):
    global dp
    
    if dp[n] == -1:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

N = int(input())
dp = [-1] * 100
dp[0] = 0
dp[1] = 1
print(fibo(N))