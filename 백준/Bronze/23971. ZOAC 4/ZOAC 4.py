# 테이블이 행마다 w개씩 h행에 걸쳐 있을 때, 모든 참가자는 세로로 n칸 또는 가로로 m칸 이상 비우고 앉기
# => n+1 x m+1 구역마다 한 명 
# => w를 n+1로 나눈 후 올림한 값 x h를 m+1로 나눈 후 올림한 값 = 최대 수용인원 
from math import ceil

h, w, n, m = map(int, input().split())
rows = ceil(h/(n+1))
cols = ceil(w/(m+1))
print(rows * cols)