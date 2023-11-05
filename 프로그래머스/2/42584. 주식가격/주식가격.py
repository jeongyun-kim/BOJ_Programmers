def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(0, len(prices)) :
        if len(stack) >= 1 :
            while stack != [] and (stack[-1][1] > prices[i]) :
                idx, price = stack.pop()
                answer[idx] = i - idx
        stack.append((i, prices[i]))
    
    for n in stack :
        idx, num = n
        answer[idx] = len(prices) - idx - 1
            
    return answer