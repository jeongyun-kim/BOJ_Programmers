def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5] # 5
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    p1, p2, p3 = 0, 0, 0
    
    for idx, ans in enumerate(answers) :
        if ans == a1[idx%5] :
            p1 += 1
        if ans == a2[idx%8] :
            p2 += 1
        if ans == a3[idx%10] :
            p3 += 1
    
    m = max(p1, p2, p3) 
    if m == p1 :
        answer.append(1)
    if m == p2 :
        answer.append(2)
    if m == p3 :
        answer.append(3)
        
    return answer