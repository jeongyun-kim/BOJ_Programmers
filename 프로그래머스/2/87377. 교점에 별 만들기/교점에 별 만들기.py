def solution(line):
    # 직선들의 교점 구하기 -> 정수로만 표현되는 좌표 가져오기
    # *, . 으로 표현 
    # 격자판의 크기 : 가로,세로 = (최댓값-최솟값)+1
    # Ax + By + E = 0 / Cx + Dy + F = 0 -> x = (BF - ED) / (AD - BC), y = (EC - AF) / (AD - BC)
    answer = []
    xs = []
    ys = []
    
    for i in range(0, len(line)-1) :
        A, B, E = line[i]
        for j in range(i+1, len(line)) :
            C, D, F = line[j]
            div = A*D - B*C
            if div != 0 :
                x = (B*F - E*D) / div
                y = (E*C - A*F) / div
            if x == int(x) and y == int(y) :
                xs.append(int(x))
                ys.append(int(y))
                
    max_x, max_y = max(xs), max(ys)
    min_x, min_y = min(xs), min(ys)
    
    w = max(xs) - min(xs) + 1
    h = max(ys) - min(ys) + 1
    points = [["."] * w for i in range(h)]
 
    for i in range(0, len(xs)) :
        x, y = xs[i], ys[i]
        px = x - min_x
        py = max_y - y
        points[py][px] = "*"
        
    for point in points :
        answer.append("".join(point))
        
    return answer