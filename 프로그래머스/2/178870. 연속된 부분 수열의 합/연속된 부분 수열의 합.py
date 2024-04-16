# 투포인터 이용
# left, right 이용해서 k를 만족하는 제일 짧은 부분 수열의 인덱스 구하기 
# sum(sequence[left:right+1]) < k : right + 1
# else : left + 1 
def solution(sequence, k):
    answer = [0, len(sequence)]
    right = 0
    total = 0

    for left in range(len(sequence)) :
        while right < len(sequence) and total < k :
            total += sequence[right]
            right += 1
        if total == k and (right-1) - left < answer[1] - answer[0] :
            answer = [left, right-1]
        total -= sequence[left]
        
                
    return answer