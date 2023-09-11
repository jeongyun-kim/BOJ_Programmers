def solution(n, lost, reserve):
    lost2 = set(lost) - set(reserve)
    reserve2 = set(reserve) - set(lost)
    
    for num in lost2 :
        if num-1 in reserve2 :
            reserve2.remove(num-1)
        elif num+1 in reserve2 :
            reserve2.remove(num+1)
        else :
            n -= 1 
            
    return n