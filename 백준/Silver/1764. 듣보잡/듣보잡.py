# n : 듣도 못한 사람의 수, m : 보도 못한 사람의 수 
# 듣보잡(듣도 못한 사람 + 보도 못한 사람)의 수와 그 명단을 사전순으로 출력 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p1 = set()
p2 = set()

for i in range(n) :
    p1.add(input().rstrip())
for j in range(m) :
    p2.add(input().rstrip())

p = sorted(p1.intersection(p2))

print(len(p))
for people in p :
    print(people)
