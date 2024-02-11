# 절단기 높이 H => 한 줄에 연속해있는 나무를 모두 절단 
# => 높이가 H보다 높은 나무는 H 위의 부분이 잘리고 그 다음, 연속해있는 나무 모두 절단 
# = H보다 큰 나무는 H 위의 부분은 잘리고 낮은 나무는 잘리지 않음 
# 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기 
n, m = map(int,input().split())
trees = sorted(list(map(int, input().split())))
start = 0
end = trees[-1]

while start <= end : 
    mid = (start + end)//2
    cnt = 0 
    for tree in trees :
        if tree > mid :
            cnt += (tree-mid)
    if cnt < m :
        end = mid - 1
    else :
        start = mid + 1 

print(end)
    