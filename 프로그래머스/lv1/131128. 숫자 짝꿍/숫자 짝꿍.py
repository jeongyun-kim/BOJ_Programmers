def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1) : # 내림차순
        answer = answer + str(i) * min(X.count(str(i)), Y.count(str(i)))
    
    if answer == '' : # answer = ""인 경우
        return '-1'
    elif len(answer) == answer.count('0') : # answer = "00"인 경우
        answer = '0'

    return answer