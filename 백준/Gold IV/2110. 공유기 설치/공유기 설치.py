# C개의 공유기를 N개의 집에 적당히 설치
# 가장 인접한 두 공유기 사이의 거리를 최대로
# 두 공유기간 최소거리는 1, 최대거리는 (가장 큰 좌표 - 가장 작은 좌표)
# xi+1 - xi >= mid : 공유기 설치, 공유기의 좌표를 xi+1로
# xi+1 - xi < mid : 공유기 설치 불가, 공유기의 좌표 유지 
# cnt > c : start = mid + 1 
# cnt <= c : end = mid - 1
n, c = map(int, input().split())
homes = sorted([int(input()) for _ in range(n)])
start = 1 # 최소 거리 
end = homes[-1] - homes[0] # 최대 거리

while start <= end :
    mid = (start + end) // 2 # 최소 거리와 최대 거리의 중간 지점 
    cnt = 1 
    nowP = homes[0] # 공유기의 좌표
    for home in homes :
        distance = home - nowP # 현재의 집 - 공유기가 설치된 위치 
        if distance >= mid : # 거리가 mid보다 크거나 같다면
            cnt += 1 # 공유기 설치 
            nowP = home # 공유기의 좌표 변경 
    if cnt >= c : # 설치된 공유기 개수가 c보다 크거나 같다면
        start = mid + 1 # 최소 거리 올리기
    else : # 설치된 공유기 개수가 c보다 작다면 
        end = mid - 1 # 최대 거리 낮추기 

# 결과 출력 
print(end)