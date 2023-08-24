def solution(arr1, arr2):
    answer = []
    num = 0
    
    for i in range(0, len(arr1)):
        arr = []
        for j in range(0, len(arr1[i])):
            num = arr1[i][j]+arr2[i][j]
            arr.append(num)
        answer.append(arr)
        
    return answer