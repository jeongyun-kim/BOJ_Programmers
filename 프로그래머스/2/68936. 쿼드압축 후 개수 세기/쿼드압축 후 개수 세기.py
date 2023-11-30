def solution(arr):
    # 1. 압축하고자 하는 특정 영역 = S
    # 2. S 내부에 있는 모든 수가 같다면 S를 해당 수 하나로 압축시키기
    # 3. 그렇지 않다면, S를 4개의 균일한 정사각형 영역으로 쪼개고 2번 반복
    answer = [0, 0]
    length = len(arr)
    
    def calc(start, end, n) :
        array = arr[start][end]
        for i in range(start, start+n) :
            for j in range(end, end+n) :
                if array != arr[i][j] : # 수가 다를 경우
                    n = n // 2
                    calc(start, end, n)
                    calc(start, end+n, n)
                    calc(start+n, end, n)
                    calc(start+n, end+n, n)
                    return 
        answer[array] += 1 # 모든 수가 같을 경우
        
    calc(0, 0, length)
    
    return answer