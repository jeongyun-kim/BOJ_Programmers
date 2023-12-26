# 입력 데이터 첫째줄: 정점의 개수N / 간선의 개수M / 탐색을 시작할 정점의 번호V
# 두번째~ : 간선이 연결하는 두 정점의 번호 
N, M, V = map(int, input().split())
# 1. 행렬 생성
matrix = [[0]*(N+1) for _ in range(N+1)]
# - 연결된 노드가 있다면 연결된 노드들에 1 표시
for i in range(M) :
     n1, n2 = map(int, input().split())
     matrix[n1][n2] = matrix[n2][n1] = 1

# 방문리스트
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

# DFS
def dfs(V) :
    visited_dfs[V] = 1 # 방문 처리 
    print(V, end = ' ')
    for i in range(1, N+1) : # V랑 연결된 노드이고 해당 노드를 방문한 적 없을 때
        if matrix[V][i] == 1 and visited_dfs[i] == 0 :
            dfs(i)

# BFS
def bfs(V) :
    queue = [V] # 첫번째로 방문한 V를 가지고 있는 queue
    visited_bfs[V] = 1
    while queue : # queue가 비어있지 않을 때
        V = queue.pop(0)
        print(V, end = ' ')
        for i in range(1, N+1) :
            if matrix[V][i] == 1 and visited_bfs[i] == 0 :
                queue.append(i)
                visited_bfs[i] = 1

# print
dfs(V)
print()
bfs(V)