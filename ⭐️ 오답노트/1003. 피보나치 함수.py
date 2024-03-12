# 백준 1003 피보나치 함수 

# 각 테스트케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해 출력 
# n은 0 이상 40 이하
t = int(input())

# ! 포인트 ! 
# 0 = 1 0 
# 1 = 0 1
# 2 = 1 1 
# 3 = 1 2 
# 현재 수의 0, 1 = 이전 수의 0, 1 + 이전 전의 수의 0, 1 

# dp 정의 
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1
for i in range(2, 41) :
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for _ in range(t) :
    idx = int(input())
    print(dp[idx][0], dp[idx][1])
