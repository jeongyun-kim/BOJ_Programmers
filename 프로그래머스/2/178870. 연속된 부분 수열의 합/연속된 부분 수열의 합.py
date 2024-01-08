# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열
# 길이가 짧은 수열이 여러 개인 경우 시작 인덱스가 작은 수열

def solution(sequence, k):
    answer = [0, len(sequence)]
    l, r = 0, 0 # 좌/우 인덱스
    total = sequence[0] # 부분 수열의 합
    
    while(1) :
        if total < k :
            r += 1 # 오른쪽으로 이동하면서 수 더하기 
            if r == len(sequence) : # r이 배열의 맨 끝에 다다른 상태면 break
                break
            total += sequence[r]
        # 부분 수열의 합이 k와 같고 현재 들어있는 수열의 길이보다 짧다면 
        elif total == k and r - l < answer[1] - answer[0] : 
                answer = [l, r]
        else : # total이 k보다 커지면 왼쪽 값 빼주고 이동
            total -= sequence[l] 
            l += 1
        
    return answer