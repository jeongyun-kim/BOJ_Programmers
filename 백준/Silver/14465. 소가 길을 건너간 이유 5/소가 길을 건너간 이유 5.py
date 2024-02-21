# 정상적으로 작동하는 연속 K개의 신호등이 존재하려면 최소 몇 개의 신호등을 수리해야 하는지
# n : 횡단보도 개수, k : 원하는 연속 횟수, b : 고장난 신호등의 개수
n, k, b = map(int, input().split())
states = [0] * (n+1) # 신호등의 상태값을 가진 배열(고장났으면 1, 아니면 0)
for i in range(b) :
    states[int(input())] = 1
j = 1
cnt, lights = 0, 0 # cnt : 수리 횟수, lights : 현재 위치까지의 횡단보도 개수 
answer = n

for i in range(1, n+1) :
    while j <= n and lights < k :
        lights += 1 
        cnt += states[j]
        j += 1
    if lights == k : 
        answer = min(answer, cnt)
    lights -= 1
    cnt -= states[i]

print(answer)
