def solution(triangle):
    answer = 0
    triangle = triangle[-1::-1]
    
    for i in range(0, len(triangle)-1) :
        for j in range(0, len(triangle[i])-1) :
            num = max(triangle[i][j], triangle[i][j+1])
            triangle[i+1][j] += num
    
    return triangle[-1][0]