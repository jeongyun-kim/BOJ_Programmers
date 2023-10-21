def solution(elements):
    arr = []
    length = len(elements)
    
    for i in range(1, length+1) :
        for j in range(0, length) :
            end = j+i 
            start = j
            # 리스트의 끝을 넘어 수를 조합할 때
            if end > length :
                total = sum(elements[start:end]) + sum(elements[:(end)%length]) 
                arr.append(total)
            else : # 아닐 때
                total = sum(elements[start:end])
                arr.append(total)
            
    return len(set(arr))