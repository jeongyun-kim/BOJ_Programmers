def solution(s):
    answer = []
    dic = {}
    
    for idx, c in enumerate(s) :
        if c not in dic.keys() : # 문자 c가 딕셔너리에 없다면 -1 삽입
            answer.append(-1)
        else : # 문자 c가 딕셔너리에 있다면 (현재 인덱스 - 최근 c의 위치) 삽입
            answer.append(idx-dic[c])
        dic[c] = idx # 문자 c의 위치 
        
    return answer