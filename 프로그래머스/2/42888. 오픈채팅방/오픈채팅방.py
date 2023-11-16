def solution(record):
    answer = []
    names = {}
    
    for re in record : # enter / change를 통한 {uid: 최종 닉네임}
        re = re.split(" ")
        if len(re) == 3 :
            eoc, uid, name = re
            names[uid] = name
    
    for re in record :
        uid = re.split(" ")[1]
        name = names[uid]
        if re[0] == "E" :
            answer.append("{}님이 들어왔습니다.".format(name))
        elif re[0] == "L" :
            answer.append("{}님이 나갔습니다.".format(name))
    
    return answer