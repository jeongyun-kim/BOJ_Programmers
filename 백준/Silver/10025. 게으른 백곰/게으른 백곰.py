# n : 얼음 양동이의 개수, x : 얼음 양동이들의 좌표
# g : 얼음 양동이 속 얼음 개수, k : 백곰이 다음 양동이까지 닿을 수 있는 거리
# 백곰이 최적의 자리를 골랐을 때 얼음의 합 구하기 = 얼음들의 합 최댓값
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
gs = []
xs = []
for i in range(n) :
    g, x = map(int, input().split())
    gs.append(g)
    xs.append(x)
distance = [0] * (max(xs)+1) # 좌표
for i in range(n) : # 각 좌표에 있는 양동이의 얼음 개수 
     distance[xs[i]] = gs[i]

slide = distance[:2*k+1] # 첫 슬라이드 
cnt = sum(slide) # 첫 슬라이드 내 얼음의 합
answer = cnt 

for j in range(1+k, len(distance)-k) : # 중심 한 칸씩 이동 
    cnt = cnt - distance[j-k-1] + distance[j+k] 
    answer = max(answer, cnt)

print(answer)