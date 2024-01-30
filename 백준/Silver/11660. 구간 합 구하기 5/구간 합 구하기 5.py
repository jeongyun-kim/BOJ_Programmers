# (x1-1, y1-1)부터 (x2-1, y2-1)까지 합 구하기 
# 그래프는 NxN
# 첫째줄 : 표의 크기 N, 합을 구해야 하는 횟수 M
# 다음 N개의 줄은 표의 형태
# 다음 M개의 줄은 합을 구해야하는 좌표
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
table = []

for i in range(n) :
    table.append(list(map(int, input().split())))

dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1) :
    for j in range(1, n+1) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i-1][j-1]

for i in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)