from itertools import combinations
def solution(nums):
    answer = 0
    num = combinations(nums, 3)
    
    for n in num :
        n = sum(n)
        cnt = 0
        for j in range(2, n) :
            if n % j == 0 :
                cnt += 1
                break
        if cnt == 0 :
            answer+=1

    return answer