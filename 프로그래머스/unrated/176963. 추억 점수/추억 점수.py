def solution(name, yearning, photos):
    answer = []
    dic = dict(zip(name, yearning))
    
    for photo in photos :
        score = 0
        for person in photo :
            if person in dic :
                score += dic[person]
        answer.append(score)
        
    return answer