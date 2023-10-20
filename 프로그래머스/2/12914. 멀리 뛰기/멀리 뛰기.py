def solution(n):
    answer = 0
    nums = [1, 2]

    for i in range(2, n) :
        nums.append((nums[i-2] + nums[i-1]) % 1234567)
    
    if n == 1 : 
        answer = 1
    elif n == 2 :
        answer = 2
    else :
        answer = nums[-1]
    
    return answer