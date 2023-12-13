def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for number in numbers :
        temp = []
        for parent in leaves :
            temp.append(parent+number)
            temp.append(parent-number)
        leaves = temp
    
    answer = leaves.count(target)
    
    return answer