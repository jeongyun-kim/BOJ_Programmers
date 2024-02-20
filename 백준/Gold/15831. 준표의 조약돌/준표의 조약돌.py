# 1. 까만색 조약돌은 b개 이하 줍기
# 2. 하얀색 조약돌은 w개 이상 줍기 
# 위 조건을 만족하는 구간이 없다면 집으로 돌아감 
# 준표와 미미가 산책할 수 있는 구간 중 가장 긴 구간의 길이 구하기 
n, b, w = map(int, input().split())
pebbles = input() # 조약돌 
colors = {'B':0, 'W':1}
j = 0
bws = [0, 0]
answer = 0 

for i in range(n) :
    while j < n : 
        # 이미 까만색 조약돌이 최대인데, 다음 돌이 검은색일 때 while문 탈출
        if bws[0] == b and pebbles[j] == 'B': 
            break
        else : # 까만색 조약돌이 넘지 않을 때 조약돌 더해주며 j 범위 넓히기 
            bws[colors[pebbles[j]]] += 1
            j += 1
    if bws[1] >= w : # 하얀색 조약돌이 최소 개수 이상인지 확인 
        answer = max(answer, sum(bws)) # 조건을 만족한다면 가장 긴 구간의 길이 구하기 
    bws[colors[pebbles[i]]] -= 1 # i 범위 증가하면서 맨앞의 조약돌 개수빼주기

print(answer)