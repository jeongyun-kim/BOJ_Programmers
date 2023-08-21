def solution(arr, divisor):
    answer = []
    arr = sorted(arr)
    
    for num in arr :
        if num % divisor == 0 :
            answer.append(num)
    
    if len(answer)>=1 :
        return answer
    else :
        return [-1]
