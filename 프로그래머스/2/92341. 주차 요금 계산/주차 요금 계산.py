import math
def solution(fees, records):
    answer = []
    arr = {}
    ins = {}
    outs = {}
    default_time, default_fee, m, m_fee = fees 
    
    for record in records :
        time, num, io = record.split(' ')
        hour, minute = map(int, time.split(":"))
        total_time = hour * 60 + minute
        if io == "IN" :
            ins[num] = total_time
        elif io == "OUT" :
            if num in outs : # 이미 사용 내역이 있으면 시간 누적으로 더하기
                outs[num] += (total_time - ins[num])
            else :
                outs[num] = total_time - ins[num]
            del ins[num] # 출차 후엔 입차 기록 지우기 
            
    # 출차 기록이 없다면 23:59분까지 이용한 것으로 간주
    max_time = 23*60 + 59
    for k, v in ins.items() :
        time = max_time - v
        if k in outs :
            outs[k] += time
        else :
            outs[k] = time
            
    # 누적 주차 시간 <= 기본 시간 : 기본 요금
    # 누적 주차 시간 > 기본 시간 : 기본 요금 + ceil(초과 시간 / 단위 시간) * 단위 요금
    for k, v in outs.items() :
        if v > default_time :
            fee = default_fee + math.ceil((v-default_time)/m) * m_fee
            arr[k] = fee
        else :
            arr[k] = default_fee
    
    # 키값 기준으로 정렬
    arr = sorted(arr.items())
    # 요금 append
    for i in arr :
        answer.append(i[1])
        
    return answer