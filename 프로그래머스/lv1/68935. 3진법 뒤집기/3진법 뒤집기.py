def solution(n):
    answer = ''

    while n > 0:			
        n, n2 = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(n2) # 3진법으로 표현한 n
        
    return int(answer, 3)