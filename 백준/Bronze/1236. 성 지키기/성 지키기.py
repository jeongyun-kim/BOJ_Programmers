# 모든 행!과 열!에 한 명 이상의 경비원이 있으면 좋겠음
# 세로 n, 가로 m (0<=n<=50)
# . : 빈칸
# x : 경비원이 있는 칸
n, m = map(int, input().split())
rows, cols = 0, 0
castle = [[0]*m for _ in range(n)]

# 해당 가로라인에 경비원이 한 명이라도 있으면 +1 하지않음
for i in range(n) :
    line = input()
    flag = False
    for j in range(m) :
        castle[i][j] = line[j]
        if "X" == line[j] :
            flag = True
    if flag == False :
        cols += 1

for i in range(m) :
    cnt = 0
    for j in range(n) :
        if "X" == castle[j][i] : # 해당 세로라인에 경비원이 있다면
            cnt += 1
    if cnt == 0 : # 없다면
        rows += 1

print(max(rows, cols))


