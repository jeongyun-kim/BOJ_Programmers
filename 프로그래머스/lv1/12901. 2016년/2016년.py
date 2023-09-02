def solution(a, b):
    answer = ''
    day31 = [1, 3, 5, 7, 8, 10, 12]
    day30 = [4, 6, 9, 11]
    days = b 
    weekday = ['THU','FRI','SAT','SUN', 'MON', 'TUE', 'WED']
    
    for month in range(1, a) :
        if month in day31 :
            days += 31
        elif month in day30 :
            days += 30
        else :
            days += 29

    answer = weekday[days % 7] 
    return answer