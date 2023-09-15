from collections import deque
def solution(s):
    answer = 0
    q = deque(s)
    
    while q :
        # 첫 글자 x 읽어옴 -> cnt1 = 1
        x = q.popleft()
        cnt1, cnt2 = 1, 0
        while q : # 첫 글자 다음 글자부터 읽기 시작
            c = q.popleft() 
            if c == x :
                cnt1 += 1
            else :
                cnt2 += 1
            if cnt1 == cnt2 : # 횟수가 같아지는 순간 break
                answer += 1
                break
        if cnt1 != cnt2 : # 두 횟수가 다른 상태에서 더 읽을 글자 X
            answer += 1
            
    return answer