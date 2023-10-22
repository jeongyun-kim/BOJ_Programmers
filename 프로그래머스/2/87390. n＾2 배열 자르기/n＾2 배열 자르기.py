def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1) :
        n1 = i % n 
        n2 = i // n
        num = max(n1, n2) + 1
        answer.append(num)
            
    return answer