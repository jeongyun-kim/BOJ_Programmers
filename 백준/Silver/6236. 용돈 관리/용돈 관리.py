# n : 며칠동안 용돈을 사용하는지, m : 통장에서 빼내 쓰는 횟수
# n ~ : i번째 날 이용할 금액 
# 현재 가진 돈 - 사용할 돈 <= 0 이면 인출(cnt+1) -> cnt == m이 되도록 
# cnt > m : start = mid + 1
# cnt <= m : end = mid - 1
import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
plans = [int(input()) for _ in range(n)]
start = max(plans) # 하루에 사용할 최대 금액이 인출 금액의 최소 단위 
end = sum(plans) # 사용할 돈을 모든 합친 금액이 인출 금액의 최대 단위 

while start <= end :
    cnt = 1 
    mid = (start + end) // 2
    money = mid 
    for plan in plans :
        money -= plan 
        if money < 0 : # 현재 가진 금액보다 계획된 금액이 크다면 
            cnt += 1 # 넣고 mid만큼 인출
            money = mid - plan # 현재 가진 돈 = 인출한 돈(mid) - 계획 금액 
    if cnt > m : # 인출 횟수 > m 
        start = mid + 1 # 인출 비용 늘리기 
    else : # 인출 횟수 <= m 
        end = mid - 1 # 인출 비용 줄이기 

# 마지막 범위값 출력 
print(end+1)