from collections import defaultdict
def solution(survey, choices):
    answer = ''
    types = ['RT', 'CF', 'JM', 'AN']
    dic = defaultdict(int) # 점수 카운트 dict
    # survey[i]의 첫번째 캐릭터는 i+1번 질문의 비동의 관련 선택지
    # survey[i]의 두번째 캐릭터는 i+1번 질문의 동의 관련 선택지
    
    # 4보다 작으면 비동의 / 4보다 크면 동의 / 4면 0점 
    for idx, choice in enumerate(choices) :
        if choice > 4 : # 동의
            dic[survey[idx][1]] += (choice-4)
        elif choice < 4 : # 비동의
            dic[survey[idx][0]] += (4-choice)
    
    for t in types :
        n = t[0] # 비동의 성격 유형
        y = t[1] # 동의 성격 유형
        if dic[n] < dic[y] : # 비동의 점수 < 동의 점수
            answer += y
        else : # 비동의 점수 > 동의 점수 / 비동의 점수 = 동의 점수(사전순)
            answer +=n 
            

    return answer