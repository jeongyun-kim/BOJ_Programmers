def solution(n):
    answer = 0
    # 1. n 다음 큰 수는 n보다 큰 자연수
    # 2. n 다음 큰 수와 n을 2진수로 변환했을 때 1의 개수는 동일
    # 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수
    cntOneInN = bin(n)[2:].count("1")
    n2 = n
    
    while(1) :
        n2 += 1
        cntOneInN2 = bin(n2)[2:].count("1")
        if cntOneInN == cntOneInN2 :
            answer = n2
            break

    return answer