from collections import defaultdict
def solution(today, terms, privacies):
    # today = 오늘 날짜 / terms = 약관종류, 유효기간 / privacies = 수집 날짜, 약관 종류
    answer = []
    t_year, t_month, t_day = today.split('.')
    dic = defaultdict()
    
    # 약관 종류 : 유효 기관 
    for term in terms :
        kind = term.split(' ')[0]
        expire = term.split(' ')[1]
        dic[kind] = expire
        
    # 날짜 계산 
    for idx, privacy in enumerate(privacies) :
        date, expire2 = privacy.split(' ')
        year, month, day = date.split('.')
        month = int(month) + int(dic[expire2])
        
        day = int(day)-1 # 유효기간이니까 보관가능일은 수집일의 일-1
        if month > 12 : # 12월을 넘어서면 year 더해주기
            year = int(year) + month // 12
            month = month % 12
            if month == 0 :
                year -= 1 
                month = 12
        elif day == 0 : # 1을 뺀 날이 0이면 ex) 2020년 1월 0일
            month -= 1 # 달을 이전 달로 돌리고 ex) 2020년 0월 0일
            day = 28 # 28일로 고정 ex) 2020년 0월 28일
            if month == 0 : # ex) 2020년 0월 28일
                year -= 1 # 1년 깎기 ex) 2019년 12월 28일
                month = 12 
        print(year, month, day)
        # 유효기간 비교
        if int(t_year) > int(year) :
            answer.append(idx+1)
        elif int(t_year) == int(year) and int(t_month) > month :
            answer.append(idx+1)
        elif int(t_year) == int(year) and int(t_month) == month and int(t_day) > day :
            answer.append(idx+1)
            
        
    return answer