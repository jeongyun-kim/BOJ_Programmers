def solution(n):
    # 가로 길이가 2, 세로 길이가 1인 직사각형모양의 타일
    # => 세로 길이가 2, 가로 길이가 n인 바닥 채우기 
    # 경우의 수를 1,000,000,007로 나눈 나머지 return
    answer = 0
    mod = 10**9+7
    dp = [0] * (n+1)
    
    if n == 0 or n == 1 :
        answer = 1
    else :
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1) :
            num = (dp[i-2] + dp[i-1]) % mod
            dp[i] = num
    
    return dp[-1]