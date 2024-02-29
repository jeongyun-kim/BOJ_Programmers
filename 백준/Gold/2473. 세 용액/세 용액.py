# 산성용액의 특성값 : 1 ~ 1,000,000,000
# 알칼리성용액의 특성값 : -1 ~ -1,000,000,000
# 같은 양의 세 가지 용액을 혼합한 용액의 특성값 = 혼합에 사용된 각 용액의 특성값의 합 
# => 0에 가장 가까운 용액을 만들고 싶음 
n = int(input()) # 전체 용액의 개수(3이상 5000이하)
potions = sorted(list(map(int, input().split()))) # 정렬된 용액들
t = abs(sum(potions[0:3])) # 0~2까지의 용액들의 특성합 
answer = [potions[0], potions[1], potions[2]] 

for i in range(n-2) :
    j = i+1 # potions[i]의 오른쪽 범위에서 첫번째 용액
    k = n-1 # potions[i]의 오른쪽 범위에서 마지막 용액 
    while j < k : 
        total = potions[i] + potions[j] + potions[k] # 세 용액의 특성합 
        if abs(total) < t : # 현재 특성합의 절댓값이 원래 특성합의 절댓값보다 작다면 
            answer[0] = potions[i]
            answer[1] = potions[j]
            answer[2] = potions[k]
            t = abs(total) # 현재 특성합의 절댓값으로 대체 
        if total <= 0 : # 특성합의 값이 <= 0 일 경우 용액 특성값 올리기
            j += 1 
        else : # 특성합의 값이 양수일 경우 용액 특성값 낮추기 
            k -= 1

for ans in answer :
    print(ans, end=" ")