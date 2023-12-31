import sys
input = sys.stdin.readline
# 첫째줄 : 테스트케이스의 개수 T
# 둘째줄 ~ : 테스트케이스 N (0<= N <=40)
# 각 테스트케이스마다 [0이 출력되는 횟수 / 1이 출력되는 횟수] 출력

# 1. 변수 정의
T = int(input())

# 2. 시간초과를 피하기 위해 dp 이용
for i in range(T) :
    num = int(input()) # 테스트케이스의 수 

    dp = [[]]*41 # 0부터 40까지 가능하므로 41칸 생성
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    dp[2] = [1, 1]

    for i in range(3, num+1) : 
        idx0 = dp[i-2][0] + dp[i-1][0]
        idx1 = dp[i-2][1] + dp[i-1][1]
        dp[i] = [idx0, idx1]
    
    print(dp[num][0], dp[num][1])