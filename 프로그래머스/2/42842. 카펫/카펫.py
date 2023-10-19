def solution(brown, yellow):
    # 카펫의 가로 길이 >= 세로 길이
    # 노란색 범위 = (가로-2)x(세로-2)
    area = brown + yellow 
    
    for i in range(2, int(area**0.5)+1) :
        if area % i == 0 :
            w = area // i
            h = i
            if yellow == (w-2)*(h-2) :
                return [w, h]
