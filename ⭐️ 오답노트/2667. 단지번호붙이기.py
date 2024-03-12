# 백준 2667 단지번호붙이기 

# 상하좌우로 붙은 집은 연결된 것
# 연결된 단지 개수 구하고 각 단지 내 집의 개수 구하기 
import sys
input = sys.stdin.readline 

n = int(input()) # 지도의 크기 n x n
cnt = 0 # 단지 내 집의 개수 
cnts = [] # 단지 내 집의 개수를 담는 배열

homes = [] # 집의 유무(1/0)을 나타내는 배열 
for i in range(n) :
    homes.append(list(map(int, input().strip())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0] * (n+1) for _ in range(n+1)] # 각 위치 방문 확인하는 배열 

def dfs(x, y) :
    global cnt # 단지 내 집의 개수 
    visited[x][y] = 1 # 현재 위치 방문 표시
    cnt += 1 # 집의 개수 + 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 좌표 범위 및 집의 유무, 방문 유무 확인 
        if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0 and homes[nx][ny] == 1 :
            dfs(nx, ny)

# 지도 돌면서
for i in range(n) :
    for j in range(n) :
        # 해당 위치에 집이 있고 방문한 적 없다면 dfs 실행 
        if homes[i][j] == 1 and visited[i][j] == 0 :
            dfs(i, j)
            cnts.append(cnt) # dfs 종료 후 해당 단지 내 집의 개수 배열에 집어넣기
            cnt = 0 # 집의 개수 다시 0으로 초기화 

# 첫번째 줄에는 총 단지수 출력
print(len(cnts))
# 다음으로 단지 내 집의 수를 오름차순으로 정렬하여 출력
cnts = sorted(cnts)
for cnt in cnts :
    print(cnt)
