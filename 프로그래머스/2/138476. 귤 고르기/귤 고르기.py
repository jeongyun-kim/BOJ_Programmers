from collections import Counter
def solution(k, tangerine):
    # dict로 바꿔서 갯수 많은것부터 넣어서 귤의 개수 충족하도록 넣기
    tangerine = Counter(tangerine)
    cnt = 0 # 크기가 서로 다른 종류의 수
    total = 0 # 판매할 과일 수
    # 갯수가 많은 순의 크기 과일
    keys = sorted(tangerine, reverse=True, key= lambda x:tangerine[x])
    
    for key in keys :
        if total >= k :
            break
        else :
            total += tangerine[key]
            cnt += 1
    
    return cnt