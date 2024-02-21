# 14465
# sliding_window
n, k, b = map(int, input().split())
states = [0] * (n+1)
for i in range(b) :
    states[int(input())] = 1

slide = states[1:k+1] # 길이 k의 slide
cnt = sum(slide) # 고장난 횡단보도의 개수 
answer = cnt 

for j in range(2, n-k+2) :
    cnt = cnt - states[j-1] + states[j+k-1] # 범위 이동 -> 맨 앞의 횡단보도 버리고 다음 횡단보도 가져옴
    answer = min(answer, cnt)

print(answer)
