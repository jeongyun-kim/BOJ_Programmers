def solution(n):
    # 1. n x n 2차원 배열
    # 2. 반시계 방향으로 배열 채우기 (1번 인덱스 +1 -> 2번 인덱스 +1 -> 1번 인덱스, 2번 인덱스 -1)
    # 3. 배열의 끝에 닿으면 방향 전환
    # 4. 마지막으로 할당할 숫자가 0이 아닐 때 정답 제
    answer = []
    arr = [[0] * i for i in range(1, n+1)]
    d_first = [1, 0, -1]
    d_second = [0, 1, -1]
    N = (n+1) * n // 2 # 들어갈 숫자들의 개수 
    df = 0 # 첫번째 인덱스
    ds = 0 # 두번째 인덱스
    d = 0 # 방향을 나타내는 수
    cnt = 0 # 숫자 넣은 횟수
    
    while cnt < N :
        arr[df][ds] = cnt + 1
        nf = df + d_first[d]
        ns = ds + d_second[d]
        if 0 <= nf < n and 0 <= ns <= nf and arr[nf][ns] == 0 : # 범위 확인
            df, ds = nf, ns
        else :
            d = (d + 1) % 3
            df += d_first[d]
            ds += d_second[d]
        cnt += 1
    
    answer = [num for nums in arr for num in nums]
    
    return answer