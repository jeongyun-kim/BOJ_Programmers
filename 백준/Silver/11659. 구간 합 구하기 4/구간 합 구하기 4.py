# n : 수의 개수, m : 합을 구해야 하는 횟수
# 둘째줄 : 수의 나열 - 1번부터 ~ n번
# 둘째줄에서 준 나열에서 i-1 ~ j-1의 합을 구하면 됨 
# 5 4 3 2 1 > 5 9 12 14 15 
# 2 4라고 하면 4(15)에서 1(9)를 빼주면 됨. 즉 dp[j] - dp[i-1]
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0]*(n+1)
for i in range(1, n+1) :
    dp[i] = dp[i-1] + nums[i-1]

for _ in range(m) :
    i, j = map(int, input().split())
    answer = dp[j] - dp[i-1]
    print(answer)
