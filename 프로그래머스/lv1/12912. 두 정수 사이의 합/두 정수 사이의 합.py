def solution(a, b):
    answer = 0
    min_i = min(a,b)
    max_i = max(a,b)
    
    for i in range(min_i,max_i+1):
        answer += i 
        
    return answer