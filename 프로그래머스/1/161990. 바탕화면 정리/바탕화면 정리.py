def solution(wallpaper):
    answer = []
    # (세로 좌표, 가로 좌표) => 빈칸은 '.' / 파일O '#'
    # 드래그 해서 파일 선택-삭제 가능
    # 드래그 한 거리는 |rdx-lux| + |rdy-luy|
    # .........
    # ....#.... (1,3) -> 가로 제일 짧은 쪽을 시작점2 / #이 처음 나오는 세로를 시작점1
    # .....##..
    # ...##.....
    # ....#..... (5,8) -> 가로 제일 긴 쪽을 끝점2+1 / #이 끝나는 세로를 끝점1+1
    
    w = []
    h = []
    for i in range(0, len(wallpaper)):
        for j in range(0, len(wallpaper[i])) :
            if wallpaper[i][j] == '#' :
                h.append(i)
                w.append(j)
                
    answer.append(min(h)) 
    answer.append(min(w))
    answer.append(max(h)+1)
    answer.append(max(w)+1)
    
    return answer