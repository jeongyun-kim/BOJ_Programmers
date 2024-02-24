# t : 테스터 데이터 구성
# n : 집의 개수
# m : 도둑이 돈을 훔칠 연속된 집의 개수 
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t) :
    n, m, k = map(int, input().split())
    homes = list(map(int, input().split()))
    money = sum(homes[:m])
    if money < k :
        answer = 1
    else :
        answer = 0
    if n != m :
        for j in range(1, n) : # 원형이니까 1부터 n-1까지 
            money -= homes[j-1]
            money += homes[(j+m-1)%n]
            if money < k :
                answer += 1
    print(answer)