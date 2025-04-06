def solution(n):
    answer = 0
    
    # dp 선언
    dp = [0] * (n+1)
    
    # dp 조건
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2   # 2를 만들 수 있는 경우의 수 : 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567