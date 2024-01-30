# N번칸, M명
# a번칸부터 b번칸까지 높이 k만큼 흙을 덮거나 파냄
# 첫째줄 : 연병장의 크기 N, 조교의 수 M
# 둘째줄 : 연병장의 각 칸의 높이 H가 순서대로 N개 주어짐
# 셋째줄 ~ : M개의 줄에 각 조교의 지시 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
order = [0] * (n+2)

for i in range(m) :
    a, b, k = map(int, input().split())
    order[a] += k
    order[b+1] -= k 

for j in range(1, n+1) :
    order[j] = order[j-1] + order[j]
    print(order[j] + arr[j-1], end = " ")