# n : 강의의 수, m : 블루레이의 개수 
n, m = map(int, input().split())
lectures = list(map(int, input().split()))
start = max(lectures) # 최소 강의 수 
end = sum(lectures) # 최대 강의 수

while start <= end :
    mid = (start + end) // 2
    cnt = 1 # 블루레이의 개수 
    size = mid # 블루레이의 크기 
    for lecture in lectures : # 블루레이 개수 계산 
        size -= lecture
        if size < 0 :
            cnt += 1
            size = mid - lecture
    if cnt > m : # 정해진 개수보다 블루레이가 많이 나온다면 크기를 증가시켜야함 
        start = mid + 1
    else : # 정해진 개수보다 블루레이가 적게 나온다면 크기를 감소시켜야함 
        end = mid - 1

print(end+1)