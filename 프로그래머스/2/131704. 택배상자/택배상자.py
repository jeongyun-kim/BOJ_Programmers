from collections import deque
def solution(orders):
    answer = 0
    container = deque([i+1 for i in range(len(orders))])
    temp = [] # 보조 컨테이너
    
    
    for order in orders :
        flag = True
        if temp :
            if order == temp[-1] :
                answer += 1
                temp.pop()
            else :
                flag = False
                
        if container :
            while order > container[0] :
                temp.append(container.popleft())
            if container[0] == order :
                flag = True
                container.popleft()
                answer += 1
        
        if flag == False :
            break
                
            
    return answer