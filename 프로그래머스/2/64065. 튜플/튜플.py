def solution(s):
    answer = []
    # 맨 앞/뒤 괄호들 지운 상태에서 },{에 구분되는 수들 나누기 -> 길이 짧은 순 정렬
    s = sorted(s[2:len(s)-2].split('},{'), key=lambda x:len(x))
    
    for c in s :
        s2 = c.split(',')
        for c2 in s2 :
            if int(c2) not in answer :
                answer.append(int(c2))
    
    return answer