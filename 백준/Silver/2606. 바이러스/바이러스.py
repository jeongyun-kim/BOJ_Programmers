# M : 컴퓨터의 개수, N : 네트워크 상에 연결된 컴퓨터 쌍의 수
M = int(input())
N = int(input())
V = 1

# 행렬 생성
matrix = [[0]*(M+1) for i in range(M+1)]
for i in range(N) :
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = matrix[v2][v1] = 1

# 방문 노드
visited = [0]*(M+1)

# BFS
queue = [V]
visited[V] = 1
while queue :
    V = queue.pop(0)
    for i in range(1, M+1) :
        if matrix[V][i] == 1 and visited[i] == 0 :
            queue.append(i)
            visited[i] = 1

print(visited.count(1)-1)