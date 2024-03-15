# 백준 7569 토마토 

# 인접한 토마토 : 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 
# n, m : 상자의 크기
# h : 쌓아올려지는 상자의 수(위, 아래)
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸 
import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 익은 토마토로부터 안 익은 토마토들이 익어가기 
def bfs() :
    while queue :
        z, x, y = queue.popleft()
        for i in range(6) : # 익은 토마토 주변을 돌면서
            nz = z + dz[i] 
            nx = x + dx[i]
            ny = y + dy[i]
            # 익은 토마토 주변에 안 익은 토마토가 있다면
            if 0<= nz < h and 0<= nx < n and 0<= ny < m and tomatoes[nz][nx][ny] == 0 :
                # 새로 익는 토마토가 익기까지의 날 = 현재 위치의 토마토가 익기까지 걸린 날 + 1일 
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1 
                # 새로 익은 토마토 주변을 돌기위해 추가 
                queue.append([nz, nx, ny])

# 몇 번째 상자 어디에 있는 토마토가 익은 토마토라면 bfs 실행 
for z in range(h) : 
    for x in range(n) :
        for y in range(m) :
            if tomatoes[z][x][y] == 1 :
                queue.append([z, x, y])

bfs()

# 상자의 모든 토마토가 익었는지 확인 
def calc() :
    answer = 0
    for i in range(h) :
        for j in range(n) :
            for k in range(m) :
                if tomatoes[i][j][k] == 0 : # 안 익은 토마토가 있다면 모두 익지 못하는 상황(-1) 반환 
                    return -1
                else : 
                    answer = max(answer, tomatoes[i][j][k])
    # 토마토가 익은 상태(1)에서 bfs를 돌기 때문에 모든 날짜에 1씩 더해져있음 
    # 그러므로 최종 날짜에서 - 1일 해주는 것이 진짜 모두 익기까지 걸린 시간 
    return answer-1 

print(calc())