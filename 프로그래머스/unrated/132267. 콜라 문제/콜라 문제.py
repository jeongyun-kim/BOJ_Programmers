def solution(a, b, n):
    answer = 0
    
    # n1 : 교환하고 받아온 병의 수 
    # n2 : 교환하고 남은 병의 수
    # n : 현재 상빈이가 가진 콜라 병의 수 
    while(n>=a) :
        n1 = (n // a) * b
        answer += n1
        n2 = n % a
        n = n1 + n2        
        
    return answer