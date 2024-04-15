# 한 유저를 여러 번 신고할 수 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리 
# k번 이상 신고된 유저는 게시판 이용이 정지, 해당 유저를 신고한 모든 유저에게 정지 사실 메일로 발송
def solution(id_list, report, k):
    answer = []
    report = set(report)
    reporters = {id:0 for id in id_list} # 신고를 한 아이디 
    reported = {id:0 for id in id_list} # 신고당한 아이디
    
    for re in report :
        id1, id2 = re.split(" ")
        reported[id2] += 1
        
    for re in report :
        id1, id2 = re.split(" ")
        if reported[id2] >= k :
            reporters[id1] += 1
            
    return list(reporters.values())