def solution(rows, columns, queries):
    answer = []
    # 행렬 생성 
    matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    
    # 행렬 테두리 회전
    for x1, y1, x2, y2 in queries :
        answer.append(rotate(matrix, x1, y1, x2, y2))

    return answer

# 테두리 회전 함수
def rotate(matrix, x1, y1, x2, y2) :
    # 회전 결과 맨 처음 숫자가 지워지기 때문에 맨 처음 숫자 저장
    first = matrix[x1-1][y1-1]
    # 가장 작은 수
    s = first
    
    # 테두리 밀기 순서 : 왼쪽 -> 아래쪽 -> 오른쪽 -> 위쪾
    # 왼쪽 테두리 밀기
    for i in range(x1, x2) :
        matrix[i-1][y1-1] = matrix[i][y1-1]
        s = min(s, matrix[i-1][y1-1])
    # 아래쪽 테두리 밀기
    for i in range(y1, y2) :
        matrix[x2-1][i-1] = matrix[x2-1][i]
        s = min(s, matrix[x2-1][i-1])
    # 오른쪽 테두리 밀기
    for i in range(x2-1, x1-1, -1) :
        matrix[i][y2-1] = matrix[i-1][y2-1]
        s = min(s, matrix[i][y2-1])
    for i in range(y2-1, y1-1, -1) :
        matrix[x1-1][i] = matrix[x1-1][i-1] 
        s = min(s, matrix[x1-1][i])
    matrix[x1-1][i] = first
    s = min(s, matrix[x1-1][i])
    
    return s
  