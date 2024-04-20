def rotate(matrix, x1, y1, x2, y2) :
    temp = matrix[x1-1][y1-1] # rotate하면서 지워질 첫번째 값
    minimum = temp # rotate 중 최솟값
    
    # 왼쪽 테두리 (아래에서 위로)
    for i in range(x1, x2) :
        matrix[i-1][y1-1] = matrix[i][y1-1]
        minimum = min(minimum, matrix[i-1][y1-1])
    # 아래 테두리 (오른쪽에서 왼쪽으로)
    for i in range(y1, y2) :
        matrix[x2-1][i-1] = matrix[x2-1][i]
        minimum = min(minimum, matrix[x2-1][i-1])
    # 오른쪽 테두리 (위쪽에서 아래쪽으로)
    # 4 <- 3 / 3 <- 2 / 2 <- 1 (x1이 2일 때, x2가 5일 때)
    for i in range(x2-1, x1-1, -1) :
        matrix[i][y2-1] = matrix[i-1][y2-1]
        minimum = min(minimum, matrix[i][y2-1])
    # 위쪽 테두리 (왼쪽에서 오른쪽으로)
    # y2-1 부터 y1-1까지 -1하면서
    for i in range(y2-1, y1-1, -1) :
        matrix[x1-1][i] = matrix[x1-1][i-1]
        minimum = min(minimum, matrix[x1-1][i])
    
    # rotate 이후, matrix[x1-1][y1] 위치에 들어가야 할 지워졌던 값 대입해주기 
    matrix[x1-1][i] = temp
    # 최솟값 반환 
    return minimum 
    
def solution(rows, columns, queries):
    answer = []
    matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    # 쿼리 돌면서 
    for query in queries :
        x1, y1, x2, y2 = query
        # 회전 중 최솟값 answer에 append
        answer.append(rotate(matrix, x1, y1, x2, y2))
    
    return answer