# dp
# n개의 줄에 m개의 숫자로 배열이 주어짐
# 1로 된 가장 큰 정사각형의 크기 구하기
# 만약 arr[i][j]가 1 이라면
# dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 
n, m = map(int, input().split())
arr = [[int(i) for i in input()] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
answer = 0

for i in range(n) :
    for j in range(m) :
        if i == 0 or j == 0 or arr[i][j] == 0 : # 맨 앞의 값이거나 주어진 배열의 [i][j]가 1 이 아니라면 
            dp[i][j] = arr[i][j] # 원래 주어진 수 대입 (1이면 1, 0이면 0)
        elif arr[i][j] == 1 : # 배열의 [i][j]가 1이라면 주위 값 중 가장 작은 값에서 +1한 후 대입
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 
        answer = max(answer, dp[i][j]) # 최대로 만들 수 있는 정사각형의 변의 길이 구하기 

# 넓이이므로 변의 길이 * 변의 길이
print(answer*answer)
