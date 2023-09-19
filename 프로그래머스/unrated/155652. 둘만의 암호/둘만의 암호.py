def solution(s, skips, index):
    answer = ''
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    # s의 문자를 index만큼 더한 문자로 변환
    # skip에 들어있는 문자는 제외하고 세지 않음
    
    for skip in skips : # skip에 들어있는 문자는 제거
        alphabets = alphabets.replace(skip, '')
    for c in s : 
        c_idx = (alphabets.index(c)+index)%len(alphabets)
        answer += alphabets[c_idx]
            
    return answer