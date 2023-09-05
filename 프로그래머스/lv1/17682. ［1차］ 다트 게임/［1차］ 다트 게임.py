def solution(dartResult):
    nums = []
    # * 은 이전값, 현재값 두 배
    # # 은 -값
    # D는 **2 / T는 **3 
    
    for c in dartResult :
        if c.isdigit() == True :
            if len(nums) >= 1 and nums[-1] == 1 and c == '0' :
                nums.pop()
                nums.append(10)
            else :
                nums.append(int(c))
        elif c == 'D' :
            nums[-1] = nums[-1] ** 2
        elif c == 'T' :
            nums[-1] = nums[-1] ** 3
        elif c == '#' :
            nums[-1] = -nums[-1]
        elif c == '*' :
            if len(nums) >= 2 :
                nums[-2] = nums[-2] * 2
                nums[-1] = nums[-1] * 2
            else :
                nums[-1] = nums[-1] * 2
                
    return sum(nums)