N = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 지도
home_map = []
for i in range(N) :
    home_map.append(list(map(int, input().strip())))

# DFS
def DFS(x, y) :
    # 범위를 넘어선다면 return False
    if x >= N or x < 0 or y >= N or y < 0 :
        return False

    # 방문한 곳에 집이 있다면 
    if home_map[x][y] == 1 :
        global cnt 
        cnt += 1 # 집 개수 + 1
        home_map[x][y] = 0 # 집 없애기 

        # 집 근처에 다른 집이 있는지 사방으로 확인
        # 근처에 집이 있다면 return True
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False # 근처에 집이 없다면 return False

# 단지 별 집의 개수
homes = []
cnt = 0

for i in range(N) :
    for j in range(N) :
        if DFS(i, j) == True :
            homes.append(cnt) 
            cnt = 0

# 첫번째 줄에는 총 단지 수 -> 단지 별 집의 수(오름차순)
homes.sort()
print(len(homes))
for home in homes :
    print(home)
