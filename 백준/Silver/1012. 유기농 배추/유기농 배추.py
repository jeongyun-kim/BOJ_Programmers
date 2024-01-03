import sys
input = sys.stdin.readline

# 첫째줄 : 테스트케이스의 개수
# 둘째줄 : 가로M, 세로N, 배추위치개수K
# ~ K : 배추의 위치
T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y) :
    q = [(x, y)]
    graph[x][y] = 0 # 방문처리
    while q :
        x, y = q.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N :
                continue
            if graph[nx][ny] == 1 :
                q.append((nx, ny))
                graph[nx][ny] = 0

# 행렬 생성 및 함수 호출 
for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]

    for i in range(K):
        n1, n2 = map(int, input().split())
        graph[n1][n2] = 1

    cnt = 0 # 필요한 배추흰지렁이 마리 수 

    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                bfs(x, y)
                cnt += 1
    # 결과 출력
    print(cnt)

