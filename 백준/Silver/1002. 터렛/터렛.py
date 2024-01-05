import math

# 첫째줄 : 테스트케이스의 개수
# 둘째줄 ~ : x1, y1, r1, x2, y2, r2
# 거리계산 : sqrt((x-x1)^2 + (y-y1)^2)
T = int(input())

for i in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 원의 중심 사이 거리 계산 
    
    if distance == 0 : # 두 원의 중심이 같을 때
        if r1 == r2 : # 두 원의 크기가 같은 경우
            print(-1)
        else : # 한 원이 다른 원 안에 들어가있을 때
            print(0)
    else : # 두 원의 중심이 다를 때
        if r1+r2 == distance or abs(r1-r2) == distance : # 외접 또는 내접일 때 
            print(1)
        elif abs(r1-r2) < distance and distance < r1+r2 : # 두 점에서 만날 때 
            print(2)
        else :
            print(0)