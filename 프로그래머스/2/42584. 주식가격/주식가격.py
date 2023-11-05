def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(0, len(prices)-1) :
        for j in range(i+1, len(prices)) :
            if prices[i] > prices[j] :
                answer[i] = j - i
                break
            else :
                answer[i] += 1
                
    return answer