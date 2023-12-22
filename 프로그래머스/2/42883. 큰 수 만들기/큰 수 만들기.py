def solution(numbers, k):
    stack = []

    for number in numbers :
        while stack and stack[-1] < number and k > 0 :
            stack.pop()
            k -= 1
        stack.append(number)
        
    if k > 0 : # ex) numbers = "91", k = 1
        stack = stack[:-k]
        
    return "".join(stack)