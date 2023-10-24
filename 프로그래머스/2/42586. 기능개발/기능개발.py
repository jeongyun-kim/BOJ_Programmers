import math
def solution(progresses, speeds):
    # progresses : 먼저 배포되어야 하는 작업들의 순서
    # speeds : 각 작업의 개발속도
    days = {}
    
    for i in range(0, len(speeds)) :
        # 각 작업별 개발 남은 일수
        day = math.ceil((100-progresses[i]) / speeds[i]) 
        # 딕셔너리가 비어있거나
        # 딕셔너리가 비지않고 이전 키의 값이 현재 개발 남은 일수보다 적을 때
        # 다음 배포 날짜잡기 (days[day]=1)
        if len(days) == 0 or (list(days.keys())[-1] < day and len(days) >= 1) :
            days[day] = 1
        # 현재 단계의 개발에 남은 일이 이전 단계의 남은 개발일보다 적거나 같게 남았을 때, 
        # 이전 개발 단계 배포 날짜에 추가해서 배포 (+1) 
        else :
            pkv = list(days.keys())[-1] 
            days[pkv] += 1
        
    return list(days.values())