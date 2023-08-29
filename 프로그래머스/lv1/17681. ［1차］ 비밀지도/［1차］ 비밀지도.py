def solution(n, arr1, arr2):
    answer = []
    arr1 = bins(arr1, n)
    arr2 = bins(arr2, n)
    
    for i in range(0, len(arr1)) :
        ans = ''
        for j in range(0, n) :
            if arr1[i][j] == '#' or arr2[i][j] == '#' :
                ans +='#'
            else :
                ans += ' '
                
        answer.append(ans)
    
    return answer

def bins(arr, n) :
    bins = []
    
    for num in arr :
        num_bin = bin(num)[2:] # 숫자를 이진수로 변환
        length = len(num_bin) # 변환된 이진수의 길이
        
        if length < n : # 변환된 이진수의 길이가 값 n보다 짧다면 앞에 0붙여서 길이 맞추기
            for i in range(0, n-length) :
                num_bin = '0' + num_bin 
        # 1을 #로 0을 공백으로 대체        
        num_bin = num_bin.replace('1','#')
        num_bin = num_bin.replace('0',' ')
        
        bins.append(num_bin)
        
    return bins
        
        