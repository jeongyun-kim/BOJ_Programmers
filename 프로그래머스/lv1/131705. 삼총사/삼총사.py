from itertools import combinations

def solution(number):
    answer = 0
    numbers = combinations(number, 3)
    
    for num in numbers :
        if sum(num) == 0 :
            answer += 1
        
    return answer