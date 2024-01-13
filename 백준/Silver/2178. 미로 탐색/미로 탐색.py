# 첫째 줄에 두 정수 N, M
# N개의 줄에는 M개의 정수로 미로가 주어짐 (no split)
# (N, M)의 위치로 이동하는 최소의 칸 수 

# 1. 변수 선언 및 초기화
rows, cols = map(int, input().split())
x, y = 0, 0 # 시작 지점
# 상하좌우 이동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 2. 행렬 생성 및 데이터 집어넣기
graph = [[]*cols for _ in range(rows)]
for i in range(rows) :
    for c in input() :
        graph[i].append(int(c))

# 3. bfs 생성
def bfs(x, y) :
    q = [(x, y)]
    while q :
        x, y = q.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols :
                continue
            if graph[nx][ny] == 1 : # 처음 방문한 곳이면
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 # 해당 위치까지 이동한 거리 = 현재 이동한 거리 + 1
    return graph[rows-1][cols-1]

# 4. 결과 출력
print(bfs(x, y))
