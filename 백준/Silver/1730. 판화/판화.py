# 지나지 않은 점은 ., 수직 방향으로만 지난 점은 |, 수평 방향으로 지난 점은 -, 수직 수평 모두 지난 점은 +
# n : 목판의 크기 (NxN), 시작 점 : (0, 0) 
n = int(input())
v = [[0 for _ in range(n)] for _ in range(n)]
h = [[0 for _ in range(n)] for _ in range(n)]
x, y = 0, 0

# 이동하면서 범위 확인 + 수평/수직 이동 확인 
for c in input() :
    if c == 'U' and y-1 >= 0 :
        v[y][x] = 1
        y -= 1
        v[y][x] = 1
    elif c == 'D' and y+1 < n :
        v[y][x] = 1
        y += 1
        v[y][x] = 1
    elif c == 'R' and x+1 < n :
        h[y][x] = 1
        x += 1
        h[y][x] = 1
    elif c == 'L' and x-1 >= 0 :
        h[y][x] = 1
        x -= 1
        h[y][x] = 1

# 흔적 출력
for i in range(n) :
    for j in range(n) :
        if h[i][j] == 1 and v[i][j] == 1 :
            print('+', end="")
        elif h[i][j] == 1 and v[i][j] == 0 :
            print('-', end="")
        elif h[i][j] == 0 and v[i][j] == 1 :
            print('|', end="")
        else :
            print('.', end="")
    print()

    