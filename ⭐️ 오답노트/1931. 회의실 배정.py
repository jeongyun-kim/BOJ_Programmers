# 각 회의에 대해 시작시간과 끝나는 시간이 주어짐 
# 회의가 겹치지 않으면서 회의실을 사용할 수 있는 회의의 최대 개수
# 회의의 시작시간과 끝나는 시간이 같은 경우도 있음
# 이는 시작하자마자 끝나는 것으로 생각할 것 
# 1. 끝나는 시간 순으로 배열 정렬
# 2. 이전 회의 끝나는 시간 <= 다음 회의 시작 시간 
import sys
input = sys.stdin.readline

n = int(input())
times = []

for i in range(n) :
    start, end = map(int, input().split())
    times.append((start, end))

times = sorted(times, key=lambda x:(x[1], x[0]))

ending = times[0][1]
cnt = 1
for i in range(1, len(times)) :
    time = times[i]
    if ending <= time[0] :
        ending = time[1]
        cnt += 1
