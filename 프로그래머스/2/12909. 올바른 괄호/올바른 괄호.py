def solution(s):
    s2 = []
    
    for c in s :
        s2.append(c)
        if len(s2) >=2 and s2[-2:] == ['(', ')'] :
            s2.pop()
            s2.pop()
    
    if len(s2) == 0 :
        answer = True
    else :
        answer = False

    return answer