# n개의 수가 주어졌을 때, 오름차순으로 정렬하여 출력
import sys
input = sys.stdin.readline

answer = []
n = int(input())

for i in range(n) :
    answer.append(int(input()))
answer = sorted(answer)

for j in range(n) :
    print(answer[j])