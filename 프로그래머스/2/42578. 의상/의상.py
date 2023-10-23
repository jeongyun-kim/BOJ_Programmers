from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict()
    
    for cloth in clothes :
        if cloth[1] not in dic :
            dic[cloth[1]] = 1
        else :
            dic[cloth[1]] += 1
        
    if len(dic) >= 2 :
        for v in dic.values() :
            answer *= (v+1) # 그 종류를 안 한 경우를 포함해서 + 1
        answer -= 1 # 아무것도 걸치지 않은 경우 제외 
    else :
        answer = len(clothes)
        
    return answer