n = int(input())
k = int(input())

start = 1 # 배열 내 가장 작은 수 
end = n*n # 배열 내 가장 큰 수 
answer = 0

while start <= end :
    mid = (start + end) // 2 # 중간값
    cnt = 0 # 중간값보다 작거나 같은 수가 몇 개나 있는지
    for i in range(1, n+1) : # 1부터 n까지의 열을 돌면서 중간값보다 작거나 같은 수가 몇 개 있는지 계산 
        cnt += min(mid//i, n)
    if cnt >= k : # 계산값이 k보다 크거나 같다면 
        answer = mid # 정답에 현재 중간값 넣고
        end = mid - 1 # 범위 줄이기
    else : # 계산값이 k보다 작다면 
        start = mid + 1 # 범위 늘리기 

# 정답 출력 
print(answer)
