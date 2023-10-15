def solution(number, limit, power):
    answer = 0
    # 1 -> 1 / 2 -> 1, 2 / 4 -> 1, 2, 4 / 6 -> 1, 2, 3, 6 / 9 -> 1, 3, 9
    
    for i in range(1, number+1) :
        cnt = 0
        for j in range(1, int(i**0.5)+1) :
            if i % j == 0 :
                cnt += 2
                if j * j == i :
                    cnt -= 1
        if cnt > limit : 
            cnt = power
        answer += cnt

    return answer