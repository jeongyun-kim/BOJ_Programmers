def solution(A,B):
    answer = 0
    # 배열 A, B에서 각각 숫자를 뽑아 곱해 더하기 => 최소
    # A는 오름차순 / B는 내림차순으로 정렬 후 곱하고 더하기 
    A.sort()
    B.sort(reverse=True)
    
    for i in range(0, len(A)) :
        answer += (A[i]*B[i])
        
    return answer