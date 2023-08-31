from itertools import combinations

def solution(numbers):
    answer = []
    nums = combinations(numbers, 2)
    
    for num in nums :
        if sum(num) not in answer :
            answer.append(sum(num))
        else :
            continue
            
    return sorted(answer)