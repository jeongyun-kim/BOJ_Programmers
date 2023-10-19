def solution(n,a,b):
    answer = 1 # 첫 라운드 카운트 
    
    while(1) :
        if a%2 != 0 : a += 1
        if b%2 != 0 : b += 1
        if a-b == 0 :
            break
        else :
            a = a // 2
            b = b // 2
            answer += 1
            
    return answer