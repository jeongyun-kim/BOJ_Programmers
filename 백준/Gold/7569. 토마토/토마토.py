# 첫 줄 : M - 상자의 가로 칸 수, N - 상자의 세로 칸 수, H - 상자의 수
# 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않음, 1 : 익은 토마토
# 익은 토마토에서 영향을 받아 익음
from collections import deque

# 1. 변수 선언 및 초기화
m, n, h = map(int, input().split())
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 방문 확인
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
q = deque()
days = 0 # 걸리는 일수 

# 2. 행렬
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 3. bfs
def bfs() :
    while q :
        x, y, z = q.popleft()
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 범위 확인 
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m or nz < 0 :
                continue
            # 안 익은 토마토가 있고 방문한 적이 없다면
            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False :
                q.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = True

# 3. q에 익은 토마토의 위치 넣고 방문 확인 
for n1 in range(h) :
    for n2 in range(n) :
        for n3 in range(m) :
            if graph[n1][n2][n3] == 1 and visited[n1][n2][n3] == False :
                q.append((n1, n2, n3))
                visited[n1][n2][n3] = True

# 4. bfs 실행 
bfs()

# 5. 최소 일수 구하기 
for line in graph :
    for arr in line :
        arr = sorted(arr)
        for tomato in arr :
            if tomato == 0 :
                print(-1)
                exit()
        days = max(days, arr[-1])

print(days-1)

