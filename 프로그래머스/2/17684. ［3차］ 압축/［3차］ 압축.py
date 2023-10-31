from collections import defaultdict
def solution(msg):
    answer = [0]
    dic = defaultdict()
    
    # A : 65 ~ Z : 90 => 사전 생성
    for i in range(0, 26) :
        dic[chr(i+65)] = i+1
    
    s2 = ""
    for s in msg :
        s2 += s
        if s2 not in dic :
            dic[s2] = len(dic) + 1
            s2 = s
            answer.append(dic[s])
        else :
            answer[-1] = dic[s2]    
            
    return answer