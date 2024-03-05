# t : 테스트케이스의 개수
# n : 맥주를 파는 편의점의 개수
# ~ : 상근이네 집, 편의점, 페스티벌 좌표 
# 한 박스에 맥주는 20병, 50미터에 한 번 맥주를 마심 -> 1000m까지가 한계 
import sys
input = sys.stdin.readline

t = int(input())
answer = ""

def bfs(x, y) :
    visited = [0] * n # 편의점 방문 표시(편의점 개수만큼)
    queue = [(x, y)] # 큐에 초깃값(상근이네 좌표) 삽입
    while queue : # 큐에 좌표가 있는 동안 
        x, y = queue.pop(0) # 현재 위치의 좌표(x, y) 가져오기 
        # 현재 위치 ~ 락 페스티벌의 거리 계산
        distance = abs(x-fes_x) + abs(y-fes_y) 
        if distance <= 1000 : # 만약 1000미터 이하라면 락 페스티벌에 도착 가능
            return "happy" # happy 
        # 현재 위치에서 락 페스티벌을 못 간다면 중간에 있는 편의점 들리기
        for i in range(n) : 
            if visited[i] == 0 : # 아직 들리지 않은 편의점이라면 
                convi_x, convi_y = conveniences[i] # 해당 편의점 좌표 가져오기 
                distance = abs(x-convi_x) + abs(y-convi_y) # 현재 위치 ~ 편의점 거리 계산
                if distance <= 1000 : # 거리가 1000미터 이하라면 편의점 들리기 
                    queue.append((convi_x, convi_y)) # 도착한 편의점 위치 queue에 삽입
                    visited[i] = 1 # 현재 
    return "sad"

# 테스트케이스 개수만큼 돌기 
for _ in range(t) :
    # 편의점의 개수 
    n = int(input()) 
    # 상근이네 좌표
    home_x, home_y = map(int, input().split()) 
    # 편의점의 좌표들 
    conveniences = [] 
    for convi in range(n) :
        convi_x, convi_y = map(int, input().split())
        conveniences.append((convi_x, convi_y))
    # 락 페스티벌의 좌표
    fes_x, fes_y = map(int, input().split())
    # bfs 계산 
    answer = bfs(home_x, home_y)
    print(answer)