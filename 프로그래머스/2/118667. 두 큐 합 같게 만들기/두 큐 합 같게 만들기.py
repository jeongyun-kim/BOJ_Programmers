from collections import deque
def solution(queue1, queue2):
    # A큐에서 pop -> B큐에 insert : 1회 => sum(A) == sum(B) : break
    q1 = deque(queue1)
    q2 = deque(queue2)
    sq1 = sum(queue1)
    sq2 = sum(queue2)
    answer = 0 
    total = sq1 + sq2
    limit = (len(q1)) * 4 # 양쪽 모두 옮겼을 때의 횟수 
    cnt = 0 # 옮긴 횟수 카운트 
    
    if total % 2 == 1 : # 큐의 원소 합이 홀수라면 절대 불가능
        answer = -1
    else :
        while(sq1 != sq2) : # [1, 1] [1, 5]처럼 불가능한 경우
            if cnt == limit :
                answer = -1
                break
            else :
                if sq1 > sq2 :
                    n = q1.popleft()
                    q2.append(n)
                    sq2 += n
                    sq1 -= n
                elif sq2 > sq1 :
                    n = q2.popleft()
                    q1.append(n)
                    sq1 += n
                    sq2 -= n
                cnt += 1
                
    if answer != -1 and cnt > 0 : answer = cnt
        
    return answer