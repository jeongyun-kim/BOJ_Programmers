# n : 보드의 크기
# 색상 : C, P, Z, Y
# 네 방면으로 모두 이동해보면 왼쪽, 위쪽은 중복되어 처리되므로 오른쪽, 아래쪽만 바꿔보기 
# 바꾼 후에는 다시 제자리로 원상태 해야 함!
import sys
input = sys.stdin.readline

# 보드의 크기 
n = int(input())
# 보드
board = [list(input()) for i in range(n)]
# 먹을 수 잇는 사탕의 최대 개수 = 정답 
answer = 0

def calc(board) :
    # 먹을 수 있는 사탕의 최대 개수 
    total = 1
    # 가로줄에서 일치하는게 몇 개 인지 확인
    for i in range(n) :
        cols = 1
        for j in range(1, n) :
            if board[i][j-1] == board[i][j] :
                cols += 1
            else :
                cols = 1
            total = max(cols, total)

    # 세로줄에서 일치하는게 몇 개 인지 확인
        rows = 1
        for j in range(1, n) :
            if board[j-1][i] == board[j][i] :
                rows += 1
            else :
                rows = 1
            total = max(rows, total)
    return total # 먹을 수 있는 사탕의 최대개수 return 

# 오른쪽 이동 : 0, +1
# 아래쪽 이동 : +1, 0
for i in range(n) :
    for j in range(n-1) :
        # 오른쪽 교환
        if j+1 < n and board[i][j] != board[i][j+1] : # 범위가 넘지 않고 오른쪽이랑 색이 다르다면 
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 오른쪽이랑 교환 
                answer = max(answer, calc(board))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 원상태로 
        if i+1 < n and board[i][j] != board[i+1][j] : # 범위가 넘지 않고 아래랑 색이 다르다면 
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 아래랑 교환 
                answer = max(answer, calc(board))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 원상태로

print(answer)


