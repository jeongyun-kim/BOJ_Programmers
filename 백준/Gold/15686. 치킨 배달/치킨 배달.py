import sys
from itertools import combinations
input = sys.stdin.readline

# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# 0 : 빈 칸, 1 : 집, 2 : 치킨집
# N : 도시의 정보(NxN), M : 폐업시키지 않을 치킨집의 최대 개수

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
answer = 100000

# 치킨집, 집 좌표 배열
chicken_xy, home_xy = [], []
distances = [] 

# 치킨집의 위치와 집의 위치 표시
for i in range(n) :
    for j in range(n) :
        if map[i][j] == 1 :
            home_xy.append([i, j])
        elif map[i][j] == 2 :
            chicken_xy.append([i, j])

# 폐업하지 않는 치킨집 M개의 위치를 임의로 가져오기
for chicken_comb in combinations(chicken_xy, m) :
    # 각 집들의 좌표: M개의 치킨집 중 해당 집과 가장 가까운 거리(치킨 거리)
    homes_dict = {(home[0], home[1]): 1000 for home in home_xy}
    # 치킨집을 하나씩 돌면서
    for chicken in chicken_comb :
        cx, cy = chicken # 현재 치킨집의 좌표 X와 Y
        for home in home_xy : # 지도에 있는 집들의 위치 가져오기
            hx, hy = home # 현재 치킨집과 비교할 집의 좌표 X와 Y
            # 현재 집의 이전 치킨거리와 현재 치킨거리를 비교해 현재 치킨집과 더 가깝다면 거리값 수정
            homes_dict[(hx, hy)] = min(homes_dict[(hx, hy)], abs(hx-cx)+abs(hy-cy))
    # 이전 도시의 치킨거리와 현재 도시의 치킨 거리를 비교해 현재 도시의 치킨 거리가 더 작다면 수정 
    answer = min(answer, (sum(homes_dict.values())))

# 결과 출력
print(answer)
