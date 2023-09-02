def solution(nums):
    n = len(nums) // 2
    nums = set(nums)
    
    if n > len(nums) :
        return len(nums)
    else : 
        return n
        