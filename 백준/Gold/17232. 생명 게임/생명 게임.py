# 첫째줄 : N - 바둑판의 세로 길이, M - 바둑판의 가로 길이, T - 바둑판 관찰 시간 
# 둘째줄 : K - 주위의 기준이 되는 정수, a/b - 각 칸의 다음 상황을 결정하는 정수 
# 생명이 있는 칸은 '*', 없는 칸은 '.'
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
K, a, b = map(int, input().split())

board = [[0] * (M + 1)] + [[0] + list(input().rstrip()) for _ in range(N)]
cnt = [[0]*(M+1) for _ in range(N+1)]

def prefixSum(N, M) :
    for i in range(1, N+1) :
        for j in range(1, M+1) :
            cnt[i][j] = cnt[i-1][j] + cnt[i][j-1] - cnt[i-1][j-1]
            if board[i][j] == '*' :
                cnt[i][j] += 1

def getSum(N, M, K, row, col, alive) :
    # 각 범위 확인
    # left : col-K-1이 0보다 작다면 0, 아니라면 col-K-1
    # right : col+K이 M보다 크다면 M, 아니라면 col+K
    left, right, up, down = max(0, col-K-1), min(col+K, M), max(0, row-K-1), min(row+K, N)
    return cnt[down][right] - cnt[down][left] - cnt[up][right] + cnt[up][left] - alive 


for t in range(T) :
    prefixSum(N, M)
    for i in range(1, N+1) :
        for j in range(1, M+1) :
            if board[i][j] == '*' :
                nearAlive = getSum(N, M, K, i, j, 1)
                if nearAlive < a or nearAlive > b : # 현재 칸에 생명이 있고 주위에 a개 미만, b개 초과의 생명이 있다면 죽음
                    board[i][j] = '.'
            else :
                nearAlive = getSum(N, M, K, i, j, 0)
                if nearAlive > a and nearAlive <= b : # 현재 칸에 생명이 없고 주위에 a개 초과 b개 이하의 생명이 있다면 탄생
                    board[i][j] = '*'

for i in range(1, N+1) :
    for j in range(1, M+1) :
        print(board[i][j], end = "")
    print()