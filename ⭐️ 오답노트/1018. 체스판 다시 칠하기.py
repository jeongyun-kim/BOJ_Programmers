# 백준 1018 체스판 다시 칠하기

# n : 보드의 가로 길이
# m : 보드의 세로 길이 (8<= n, m <= 50)
# 보드에서 8x8만큼 잘라냈을 때, 해당 칸에서 색칠하는 최소 횟수 
# B와 W는 번갈아 나옴

# ex) 시작이 w일 때 
# 00 : w / 01 : b / 02 : w / 03 : b 
# 10 : b / 11 : w / 12 : b / 13 : w
# 20 : w / 21 : b / 22 : w / 23 : b  
# => row + col -> 홀수면 b / 짝수면 w

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = 100

# 현재의 좌표 받아와 현재 좌표 포함 8x8 돌기 
def calc(i, j) :
    case1 = "BW"
    case2 = "WB"
    cnt1, cnt2 = 0, 0 # 각 케이스별 칠해야 하는 정사각형 개수
    for k in range(i, i+8) :
        for h in range(j, j+8) :
            idx = (k+h)%2 # ex) idx = 0, case = "BW"
            if board[k][h] != case1[idx] : # case[idx] = B 인데 board의 정사각형은 W일 때 
                cnt1 += 1 # 정사각형 B로 칠하기 
            if board[k][h] != case2[idx] : # case = "WB"
                cnt2 += 1
    return min(cnt1, cnt2)

for i in range(n-8+1) :
    for j in range(m-8+1) :
        cnt = calc(i, j)
        answer = min(answer, cnt) # 칠해야 하는 정사각형의 최소 개수

print(answer)
