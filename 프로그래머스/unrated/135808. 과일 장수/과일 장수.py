def solution(k, m, scores):
    answer = 0
    scores = sorted(scores, reverse=True)
    
    for i in range(0, len(scores)-m+1, m):
        arr = scores[i:i+m]
        score = arr[-1] * m 
        answer += score
        
    return answer