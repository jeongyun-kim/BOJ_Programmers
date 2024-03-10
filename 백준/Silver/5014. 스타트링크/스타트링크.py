# 스타트링크는 총 F층이 있는 고층 건물의 G층에 있음
# 강호의 현재 위치 : S층 => G층으로 가고싶음
# U : 위로 U층을 가는 버튼
# D : 아래로 D층을 가는 버튼
# ! 만약 U층 위 / D층 아래에 해당하는 층이 없으면 엘리베이터는 움직이지 않음
# = 1<= 이동 위치 <= f
f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1) # 각 층을 방문할 때 버튼을 누른 횟수 저장하는 배열 

def bfs() :
    queue = [s]
    visited[s] = 1 # 처음 위치 방문 표시
    while queue :
        # 현재 방문한 층
        now_floor = queue.pop(0)
        if now_floor == g : # 현재 방문한 층 = 스타트링크 사무실이라면 
            # 현재 층까지 오는데 버튼 누른 횟수 반환
            # 1층에서 카운트 1을 해줬기 때문에 결과에서 -1
            return visited[now_floor]-1 
        else :
            # 현재 층에서 이동할 수 있는 층(d층 아래, u층 위)
            for next_floor in (now_floor-d, now_floor+u) :
                # 다음 층이 1층 이상 f층 이하 + 방문한 적 없는 층이라면
                if 1<= next_floor <= f and visited[next_floor] == 0 :
                    # 아래/위로 이동한 층에 이동 전 층까지 누른 버튼 횟수에 +1
                    visited[next_floor] = visited[now_floor] + 1
                    # 이동한 층 추가
                    queue.append(next_floor)
    # 만약 엘리베이터로 스타트링크 사무실을 갈 수 없다면 -1 반환 
    return "use the stairs"

# 결과 
answer = bfs()
print(answer)