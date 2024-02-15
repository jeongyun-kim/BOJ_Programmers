# n : 학생의 수, m : 보석 색상의 수 
# 보석은 같은 색상의 보석끼리만 가질 수 있음, 받아가지 못하는 학생이 있을 수 있음 
# 각 보석의 색상 % mid == 0 => 각 보석의 색상 // mid가 해당 보석을 가져간 사람 수
# 각 보석의 색상 % mid != 0 => 각 보석의 색상 // mid + 1 가 해당 보석을 가져간 사람 수 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewels = [int(input()) for _ in range(m)]
start = 1 # 한 명이 가져갈 수 있는 최소 개수 
end = sum(jewels) # 한 명이 가져갈 수 있는 최대 개수

while start <= end :
    mid = (start + end) // 2
    students = 0 # 보석을 가져간 사람 수 
    for jewel in jewels : # 각 보석의 개수를 돌면서 
        if jewel % mid == 0 : # 보석을 공평하게 배분할 수 있으면  
            students += (jewel // mid)
        else : # 보석을 공평하게 배분할 수 없으면 
            students += (jewel // mid + 1)
    if students > n : # 보석을 배분받은 학생의 수가 주어진 학생보다 많으면 
        start = mid + 1 # 인당 가져갈 수 있는 보석의 개수 증가 
    else : # 보석을 배분받은 학생의 수가 주어진 학생보다 적으면
        end = mid - 1 # 인당 가져갈 수 있는 보석의 개수 감소 

print(end+1)