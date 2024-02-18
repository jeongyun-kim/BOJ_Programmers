# n : 수열의 길이, m : 수의 차이 
# 수열에서 두 수를 골랐을 때(같은 수일 수도 있음) 그 차이가 m 이상이면서 제일 작은 경우
# diff < m : j + 1
# diff > m : i + 1, answer = min(diff, answer)
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
j, diff = 0, 0
answer = 2e+9+1

for i in range(n) :
    while arr[j] - arr[i] < m and j < n-1 : # 두 수의 차이가 m의 이상이 되기전까지 j 증가 
        j += 1
    # 두 수의 차이가 m 이상일 때, 두 수의 차이를 구하기
    # 이전 while문에서 j < n 으로 했을 때, 마지막 인덱스까지 포함되고 그럼 결국 j == n이 나옴
    # 그럼 diff 계산식의 arr[j]가 인덱스 에러를 일으킴
    # => 그렇기 때문에 조건이 j < n이 아닌 j < n-1이 됨 
    diff = arr[j] - arr[i] 
    if diff >= m :
        answer = min(answer, diff)

print(answer)