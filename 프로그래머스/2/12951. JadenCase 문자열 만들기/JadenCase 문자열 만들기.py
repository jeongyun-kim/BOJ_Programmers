# JadenCase : 모든 단어의 첫 문자가 대문자, 그 외는 소문자인 문자열

def solution(s):
    answer = ' '
    
    for c in s.lower() :
        if answer[-1] == ' ' :
            if c.isalpha() :
                answer += c.upper()
            else :
                answer += c
        else :
            answer += c  
        
    return answer[1:]