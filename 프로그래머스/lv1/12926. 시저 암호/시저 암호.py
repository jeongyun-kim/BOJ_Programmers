def solution(s, n):
    answer = ''
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    
    for c in s : # 대문자
        if c in uppers :
            idx = (uppers.index(c) + n) % 26
            answer += uppers[idx]
        elif c in lowers : # 소문자
            idx = (lowers.index(c) + n) % 26
            answer += lowers[idx]
        else : # 공백
            answer += c
        
    return answer