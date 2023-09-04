def solution(N, stages):
    answer = {}
    players = len(stages)
    
    for i in range(1, N+1) :
        if players != 0 : 
            p = stages.count(i) # 도달만 한 유저 수
            clear_x = p / players # 실패율
            answer[i] = clear_x
            players -= p
        else :
            answer[i] = 0

    answer = sorted(answer, key = lambda x:answer[x], reverse=True)
    
    return answer