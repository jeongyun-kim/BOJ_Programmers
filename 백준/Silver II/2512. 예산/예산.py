# 1. 모든 요청이 배정될 수 있는 경우, 요청한 금액을 그대로 배정
# 2. 모든 요청이 배정될 수 없는 경우, 특정한 정수 상한액을 계산하여 그 이상인 요청에 상한액을 배정
# n : 지방의 수, m : 총 예산
# 배정된 예산들 중 최댓값 출력 
# start : 1, end : 예산의 최댓값 
n = int(input())
plans = sorted(list(map(int, input().split())))
m = int(input())
start = 1
end = plans[-1]

while start <= end :
        mid = (start + end) // 2 # 상한액 
        total = 0 # 계산될 총 예산 
        for plan in plans :
            if plan <= mid : # 예정 금액 <= mid : 총 예산 + 예정 금액
                total += plan
            else : # 예정 금액 > mid : 총 예산 + mid 
                total += mid 
        if total > m : # 총 예산 > m(정해진 총 예산) : 예산 줄이기위해 end 감소
            end = mid - 1
        else : # 총 예산 <= m(정해진 총 예산) : 예산 늘리기위해 start 증가
            start = mid + 1
print(end) # 상한액 출력 