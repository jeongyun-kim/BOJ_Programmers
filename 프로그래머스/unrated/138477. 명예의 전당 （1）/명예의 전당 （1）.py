def solution(k, scores):
    answer = []
    arr = []
    
    for score in scores :
        arr.append(score)
        if len(arr) > k :
            arr.remove(min(arr))
        answer.append(min(arr))
        
    return answer