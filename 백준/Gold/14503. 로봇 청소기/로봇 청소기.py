# 로봇청소기가 있는 방은 N x M
# 청소기는 동, 서 남, 북 방향을 바라봄 
# 방의 각 칸은 좌표 (r, c) / 가장 서북쪽은 (0, 0) / 가장 동남쪽은 (n-1, m-1)
# => 좌표 (r, c) = 북쪽에서 (r+1)번째 줄의 서쪽의 (c+1)번째 칸
# 1. 현재 칸이 청소되지 않은 경우 현재 칸을 청소
# 2. 현재 칸 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
# 2-1. 바라보는 방향을 유치한 채로 한 칸 후진하고 1번으로 돌아감
# 2-2. 바라보는 방향의 뒤칸이 벽이라 후진할 수 없다면 작동 멈춤(x 좌표가 0이라면 작동 멈춤)
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
# 3-1. 반시계 방향으로 90도 회전
# 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한 칸 전진 
# d : 북0 / 1동 / 2남 / 3서
from collections import deque
import sys
input = sys.stdin.readline

# 방의 크기 N x M
n, m = map(int, input().split())

# 이동방향 : 북 - 동 - 남 - 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 로봇청소기의 처음 좌표와 바라보고 있는 방향 
r, c, d = map(int, input().split())

# 각 장소의 좌표(r, c)와 상태(0이면 청소되지 않은 빈칸, 1이면 벽이 있는 것)
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y, d) :
    queue = deque()
    answer = 0

    queue.append((x, y, d))
    graph[x][y] = 2
    answer += 1

    while queue :
        x, y, d = queue.popleft()
        temp_d = d
        turn = 0
        for _ in range(4) :
            nd = (temp_d+3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            temp_d = nd
            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = 2
                    answer += 1
                    queue.append((nx, ny, nd))
                    break
                else :
                    turn += 1
        if turn == 4 :
            nx2 = x + dx[(d+2)%4]
            ny2 = y + dy[(d+2)%4]
            if graph[nx2][ny2] == 1 : # 후진하려는데 해당 위치가 벽이라면 작동 멈추기 
                return answer 
            queue.append((nx2, ny2, d))

print(bfs(r, c, d))