# 로그에는 어떤 사람이 들어왔는지, 나갔는지가 기록됨
# 로그가 주어졌을 때, 회사에 있는 모든 사람을 구하기 -> 이름 사전순 역순(동명이인X)
# enter : 출근, leave : 퇴근 
import sys
input = sys.stdin.readline

n = int(input())
answer = set()

for i in range(n) :
    name, io = input().split()
    if name not in answer : # 출입기록이 없다면 들어온 것이므로 enter 처리
        answer.add(name)
    else : # 출입기록이 존재한다면 출근한 전적이 있으므로 leave 처리 
        answer.remove(name)

answer = sorted(answer, reverse=True)

for j in range(len(answer)) :
    print(answer[j])
