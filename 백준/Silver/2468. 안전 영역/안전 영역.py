# n : 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수
# 비의 양을 0부터 100까지 돌면서 안전한 영역이 최대의 개수가 생길 때
# 안전 영역이 최대일 때의 개수 구하기
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
areas = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, areas))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0

def dfs(x, y, h) :
    visited[x][y] = 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0 and areas[nx][ny] > h :
            visited[nx][ny] = 1
            dfs(nx, ny, h)

for h in range(101) :
    safe_area = 0 # 안전영역 카운트 
    visited = [[0]*(n+1) for _ in range(n+1)] # 각 구역 방문했는지 확인하는 배열
    for i in range(n) : 
        for j in range(n) :
            # 물에 잠기지 않으면서 방문한 적 없는 영역일 때
            if areas[i][j] > h and visited[i][j] == 0 :
                dfs(i, j, h)
                safe_area += 1
    answer = max(answer, safe_area)

print(answer)