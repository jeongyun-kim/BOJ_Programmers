def solution(park, routes):
    # 주어진 방향으로 이동 시 공원을 벗어나는지
    # 주어진 방향으로 이동 중 장애물을 만나는지
    # => 이 둘 중 하나라도 해당되면 명령을 무시하고 다음 명령 수행
    # pakrk : 공원 / routes : 수행할 명령
    # S : 시작점 / O : 이동 가능한 통로 / X : 장애물
    directions = {'E':(0,1), 'S':(1,0), 'W':(0,-1), 'N':(-1,0)}
    for idx,p in enumerate(park) :
        for idx2, yn in enumerate(p) :
            if yn == 'S' :
                d = [idx, idx2]

    for route in routes :
        flag = True
        direction, num = route.split(' ')
        d1, d2 = d
        for i in range(0, int(num)) :
            d1 = d1 + directions[direction][0]
            d2 = d2 + directions[direction][1]
            if d1 >= len(park) or d1 < 0 or d2 < 0 or d2 >= len(park[0]) or park[d1][d2] == 'X' :
                flag = False
                break
        if flag == True :
            d = [d1, d2]
        
    return d