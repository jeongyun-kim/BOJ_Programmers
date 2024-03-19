# 백준 3085 사탕 게임

# 처음에 NxN 크기에 사탕을 채워넣음
# 사탕의 색이 다른 인접한 두 칸을 고름 => 서로 교환 => 모두 같은 색이 이루어져 있는 가장 긴 부분의 사탕 개수 
# 교환은 오른쪽, 아래쪽으로 이루어짐 
n = int(input())
candies = [list(input().strip()) for _ in range(n)]
answer = 0

def calc(candies) :
    total = 1
    for i in range(n) :
        cols = 1
        # 가로줄 확인 
        for col in range(n-1) :
            if candies[i][col] == candies[i][col+1] :
                cols += 1
            else : 
                cols = 1
            total = max(total, cols)
        # 세로줄 확인
        rows = 1
        for row in range(n-1) :
            if candies[row][i] == candies[row+1][i] :
                rows += 1
            else :
                rows = 1
            total = max(total, rows)
    return total # 먹을 수 있는 사탕의 최대개수 return 

for i in range(n) :
    for j in range(n) :
        # 오른쪽 범위 및 색 다른지 확인
        if j+1 < n and candies[i][j] != candies[i][j+1] :
            # 교환
            candies[i][j+1], candies[i][j] = candies[i][j], candies[i][j+1]
            answer = max(answer, calc(candies))
            candies[i][j+1], candies[i][j] = candies[i][j], candies[i][j+1]
        # 아래쪽 범위 및 색 다른지 확인
        if i+1 < n and candies[i][j] != candies[i+1][j] :
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            answer = max(answer, calc(candies))
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

print(answer)
