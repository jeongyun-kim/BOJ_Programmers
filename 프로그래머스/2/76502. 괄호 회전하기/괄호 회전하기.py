def solution(s):
    # () / [] / {} 올바른 괄호문자열
    # 맨 앞의 괄호를 맨뒤로 보내면서 회전시켰을 때
    # 올바른 괄호문자열의 개수
    answer = 0
    
    for i in range(0, len(s)) :
        s2 = s
        while('[]' in s2 or '()' in s2 or '{}' in s2) :
            s2 = s2.replace('[]', '')
            s2 = s2.replace('()', '')
            s2 = s2.replace('{}', '')
        if len(s2) == 0 :
            answer += 1
        s = s[1:] + s[0]
        
    return answer