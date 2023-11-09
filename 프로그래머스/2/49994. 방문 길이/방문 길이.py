def solution(dirs):
    directions = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    positions = {} # 갔던 길인지 체크
    x, y = 0, 0
    
    for d in dirs :
        dx = x + directions[d][0]
        dy = y + directions[d][1]
        if abs(dx) > 5 or abs(dy) > 5 : # 경계를 넘으면 건너뛰기 
            continue
        else:
            prex, prey = x, y # 이동하기 전 좌표
            x, y = dx, dy # 이동 후 좌표
            way = (prex, prey, x, y)
            re_way = (x, y, prex, prey)
            if way not in positions : # 이동 전 좌표 - 이동 후 좌표
                if re_way not in positions : # 같은 길로 돌아온 경우가 있다면
                    positions[way] = 1

    return len(positions)