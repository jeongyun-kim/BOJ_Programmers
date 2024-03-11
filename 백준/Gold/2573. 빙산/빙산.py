# 빙산 외 바다는 0
# 빙산은 매년 동서남북 네 방향으로 붙어있는 0(바다)의 개수만큼 줄어듦 but 0 이상 
# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년) 구하기 
# ! 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0 출력
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
year = 0

def bfs(x, y) :
    queue = deque([(x, y)])
    visited[x][y] = 1 
    near_sea = [] # 주변에 바다가 몇 개 있는 저장할 배열
    while queue :
        x, y = queue.popleft()
        cnt = 0 # 주위 바다 개수
        # 주위 돌면서 바다 개수 체크 + 구역 넓히기 
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m : 
                if visited[nx][ny] == 0 and ices[nx][ny] > 0 : # 방문한 적 없고 빙산이라면 
                    visited[nx][ny] = 1 # 방문 처리
                    queue.append((nx, ny)) # 다음으로 방문할 빙산 저장
                elif ices[nx][ny] == 0 : # 바다라면 
                    cnt += 1 # 바다 개수 카운트
        if cnt > 0 : # 주변에 바다가 있다면 
            near_sea.append((x, y, cnt)) # 주변에 바다를 둔 빙산의 좌표와 주변 바다의 수 저장 
    for x, y, cnt in near_sea : # 
        ices[x][y] = max(0, ices[x][y] - cnt)
    return 1 

# 빙산의 위치 좌표만 가진 배열 
ices_xy = []
for i in range(n) :
    for j in range(m) :
        if ices[i][j] > 0 : 
            ices_xy.append((i, j))

# 빙산이 존재할 땐 계속해서 while문 돌기 
while ices_xy :
    visited = [[0]*m for _ in range(n)]
    link = 0
    ice_to_sea = [] # 빙산이 바다로 녹아내린 경우의 좌표 
    for x, y in ices_xy :
        if visited[x][y] == 0 and ices[x][y] > 0 :
            link += bfs(x, y)
        if ices[x][y] == 0 :
            ice_to_sea.append((x, y))
    if link >= 2 : # 구역이 2개 이상이라면 
        print(year) 
        break
    # 현재 빙산이 있는 좌표 업데이트 
    # 이후 빙산의 좌표 = 업데이트 전 빙산의 좌표 - 빙산에서 바다가 되어버린 좌표
    ices_xy = sorted(list(set(ices_xy) - set(ice_to_sea)))
    year += 1 # 1년 지나기 

if link < 2 :
    print(0)
    