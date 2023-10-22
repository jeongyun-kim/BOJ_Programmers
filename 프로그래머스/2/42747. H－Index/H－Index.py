def solution(citations):
    # n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
    # h의 최댓값이 이 과학자의 H-Index
    answer = len(citations) # ex) [5,5,5,5,5]
    citations = sorted(citations, reverse=True)
    
    for idx, citation in enumerate(citations) :
        if idx >= citation :
            answer = idx
            break

    return answer