def solution(babbling):
    answer = 0
    says = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        for say in says:
            if say*2 not in b:
                b = b.replace(say,' ')
        if len(b.strip()) == 0 :
            answer += 1
            
    return answer