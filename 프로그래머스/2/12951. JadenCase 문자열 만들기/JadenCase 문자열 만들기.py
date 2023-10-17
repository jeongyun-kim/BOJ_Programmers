def solution(s):
    # JadenCase : 모든 단어의 첫 문자가 대문자, 그 외는 소문자
    # 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자
    s = s.lower()
    answer = s[0].upper()
    
    for i in range(1, len(s)):
        if answer[-1] == ' ' :
            answer += s[i].upper()
        else :
            answer += s[i]
            
    return answer
