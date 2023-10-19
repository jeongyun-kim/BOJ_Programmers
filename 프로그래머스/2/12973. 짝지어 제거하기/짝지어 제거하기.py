def solution(s):
    answer = -1
    # 알파벳 2개가 붙어있으면 제거 => 모두 제거 가능하면 1 / 아니면 0
    s2 = []
    
    for c in s :
        if len(s2) >= 1 and s2[-1] == c :
            s2.pop()
        else :
            s2.append(c)
    
    if len(s2) == 0 :
        answer = 1
    else :
        answer = 0
        
    return answer