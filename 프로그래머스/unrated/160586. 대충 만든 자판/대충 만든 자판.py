def solution(keymap, targets):
    answer = []
    dic = {}
    
    # 1번키 idx를 갖고있다가 더 작은 값이 나오면 교체 
    for keys in keymap :
        for idx, c in enumerate(keys) :
            if c not in dic :
                dic[c] = idx+1
            elif c in dic and dic[c] > idx :
                 dic[c] = idx+1
                    
    for target in targets :
        total = 0
        for c2 in target :
            if c2 in dic :
                total = total + dic[c2]
            else :
                total = -1
                break
                
        answer.append(total)
                
    return answer