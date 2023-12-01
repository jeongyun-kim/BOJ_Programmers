def solution(numbers):
    # 짝수의 경우는 +1, 홀수는 (원래수+2**(원래수의 끝쪽 1의 개수-1))
    answer = []

    for num in numbers :
        if num % 2 == 0 : 
            answer.append(num+1)
        else :
            b = bin(num).replace('b', '0')
            b = b[-1::-1].index('0') # 0이 처음 나오는 위치 = bin(num)끝쪽 1의 개수
            answer.append(num+2**(b-1))
            
    return answer