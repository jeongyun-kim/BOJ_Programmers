def solution(n):
    answer = 0
    n = str(n)
    
    for c in n :
        answer += int(c)

    return answer