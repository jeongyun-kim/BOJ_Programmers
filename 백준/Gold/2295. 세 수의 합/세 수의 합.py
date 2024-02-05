# 첫째줄에 자연수 N
# N개의 줄에 U의 원소가 하나씩 주어짐
# 집합 내의 세 수를 골라 더한 합이 집합에 들어있으면서 가장 큰 경우 출력
# a+b+c = x => a+b = x-c

n = int(input())
u = [int(input()) for _ in range(n)]
u = sorted(u, reverse=True)
sums = set()

for i in range(n) :
    for j in range(i, n) :
        sums.add(u[i] + u[j])

flag = 0

for i in range(len(u)) :
    for j in range(i, len(u)) :
        if u[i] - u[j] in sums :
            print(u[i])
            flag = 1
            break
    if flag == 1 :
        break