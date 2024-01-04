def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs(x, y) :
            q = []
            q.append((x,y))

            while q :
                x, y = q.pop(0)
                for i in range(4) :
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m :
                        continue
                    if maps[nx][ny] == 1 : # 처음 방문한 곳이면 상하좌우 확인 
                        q.append((nx, ny))
                        maps[nx][ny] = maps[x][y] + 1 
                        print(nx, ny, maps[nx][ny])
            return maps[n-1][m-1] # 상대 진영까지의 거리 반환
    
    answer = bfs(0, 0)
    
    if answer == 1 : # 벽으로 막혀서 도착하지 못했다면 1 반환
        answer = -1
                
    return answer
