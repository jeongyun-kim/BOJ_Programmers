def solution(arr):
    m_idx = arr.index(min(arr))
    del(arr[m_idx])
    
    if len(arr)>=1 :
        return arr
    else :
        return [-1]
    