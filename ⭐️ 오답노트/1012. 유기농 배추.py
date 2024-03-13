# 백준 1012 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 테스트케이스의 개수 
t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnts = [] 

# dfs 정의 
def dfs(x, y) :
    visited[x][y] = 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1 :
            dfs(nx, ny)

for _ in range(t) :
    # 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수 
    m, n, k = map(int, input().split())
    visited = [[0]*m for _ in range(n)] # 방문 확인할 배열
    graph = [[0]*m for _ in range(n)] # 배추가 있는 곳 표시할 배열 
    cnt = 0 # 필요한 배추흰지렁이 마리 수 
    # graph에 각 배추가 있는 좌표 넣어주기 
    for _ in range(k) :
        col, row = map(int, input().split())
        graph[row][col] = 1
    # 그래프 돌면서
    for i in range(n) :
        for j in range(m) :
            # 방문한 적도 없고 현재 위치에 배추가 있다면 
            if visited[i][j] == 0 and graph[i][j] == 1 :
                dfs(i, j) # dfs 진입
                cnt += 1 # 배추흰지렁이 + 1
    # 각 배추밭에 필요한 배추흰지렁이 집어넣기 
    cnts.append(cnt)

# 결과 출력            
print(*cnts)
