# 원형 : % 이용
# 시계방향 + 반시계방향 = sum(points)
# answer = max(min(left, right), answer)
n = int(input()) 
points = [int(input()) for _ in range(n)]
total = sum(points)
right = points[0] # 시계 방향
left = total - right # 반시계 방향 
answer = max(min(left, right), 0)
j = 1 # 시계 방향으로 도는 인덱스 

for i in range(n) :
    while right < left : 
        right += points[j%n] # 시계방향쪽 범위 증가에 따른 거리 증가 
        left = total - right # total - 시계방향쪽 거리 = 반시계방향쪽 거리 
        j += 1 # 시계 방향으로 범위 증가 
    # if right >= left면 answer 비교 후 변경
    answer = max(min(right, left), answer)
    # 시계방향쪽 시작 지점을 우측으로 한 칸 이동하며 시계방향쪽 거리에서 이전 시작 지점 거리 빼주기 
    right -= points[i] 
    # 시계방향쪽 거리의 시작 지점이 변경됨에 따라 시계반대방향쪽의 끝지점이 증가 
    left += points[i]

print(answer)