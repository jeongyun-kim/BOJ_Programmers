# K : 가지고 있는 랜선의 개수, N : 필요한 랜선의 개수 
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
start = 1
end = max(lines)

while start <= end :
    mid = (start + end) // 2
    cnt = 0
    for line in lines :
        cnt += (line//mid)
    if cnt >= n :
        start = mid + 1
    else : 
        end = mid - 1

print(end)
