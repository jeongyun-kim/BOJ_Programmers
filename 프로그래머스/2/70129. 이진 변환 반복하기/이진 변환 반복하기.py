def solution(s):
    # 1. x의 모든 0 제거
    # 2. x의 길이 c => c를 2진법으로 표현한 문자열
    # ! s가 1이 될 때 까지 계속해서 이진 변환
    cnt_zero, cnt = 0, 0
    
    while (s != "1") :
        cnt += 1 # 이진 변환을 가한 횟수
        before = len(s) # 0 지우기 전 길이
        s = s.replace('0','')
        after = len(s) # 0 지운 후 길이
        cnt_zero += (before - after) # 지운 0의 갯수
        s = bin(after)[2:] # 이진수 변환 후 문자열      
    
    return [cnt, cnt_zero]