def solution(food):
    answer = ''
    s = ''
    
    for idx, num in enumerate(food) :
        if num >= 2 :
            for i in range(0, num//2) :
                s = s + str(idx)
                
    answer = s + '0' + s[-1::-1]
    return answer