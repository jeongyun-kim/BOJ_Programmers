def solution(id_list, report, k):
    # 각 유저는 한 번에 한 명의 유저 신고 가능 -> 동일 유저 신고는 1회로 처리 => 중복 제거
    report = list(set(report))
    reported = {name:0 for name in id_list} # 신고당한 사람
    reporter = {name:0 for name in id_list} # 신고한 사람
    
    # k번 이상 신고된 유저는 정지 -> 신고한 모든 유저에게 정지 사실을 메일로 발송
    for r in report : # 신고 카운트
        reported_p = r.split(' ')[1] # r1은 신고한 사람, r2는 신고당한 사람
        reported[reported_p] += 1
    
    for r in report : 
        reporter_p, reported_p = r.split(' ') 
        if reported[reported_p] >= k : # 당한 이가 신고 횟수가 k이상이면
            reporter[reporter_p] += 1 # 메일 발송
    
    return list(reporter.values())