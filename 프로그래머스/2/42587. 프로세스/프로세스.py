from collections import deque
def solution(priorities, location):
    # 1. 실행 대기 큐에서 대기중인 프로세스를 하나 꺼냄
    # 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은게 있다면 꺼낸거 다시 집어넣음
    # 3. 만약 우선순위 더 높은게 없다면 방금 꺼낸 프로세스 실행 => 큐에 다시 넣지않고 종료
    p2 = deque(priorities)
    # 프로세스의 인덱스
    idxs = deque([i for i in range(0, len(priorities))])
    answer = []
    
    while(len(p2) > 0) :
        idx = idxs.popleft()
        if p2[0] < max(p2) :
            p2.append(p2.popleft())
            idxs.append(idx)
        elif p2[0] == max(p2) :
            p2.popleft()
            answer.append(idx)
            if idx == location :
                break
            
    return len(answer)