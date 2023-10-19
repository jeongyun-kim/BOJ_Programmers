def solution(arr):
    arr = sorted(arr)
    
    # 두 수의 최소공배수를 넣어가면서 모든 수의 최소공배수 구하기
    for i in range(0, len(arr)-1) :
        num = arr[i] * arr[i+1] 
        for j in range(2, num+1) : 
            if j % arr[i] == 0 and j % arr[i+1] == 0 :
                arr[i+1] = j
                break

    return arr[-1]