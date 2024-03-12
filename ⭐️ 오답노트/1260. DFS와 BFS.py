# 백준 1260 DFS와 BFS

# DFS로 탐색한 결과와 BFS로 탐색한 결과 출력
# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
# 더 이상 방문할 수 있는 점이 없을 때 종료
n, m, v = map(int, input().split())
vs = [[0] * (n+1) for _ in range(n+1)] # 간선이 연결하는 두 정점 나타내는 배열
for i in range(m) :
    n1, n2 = map(int, input().split())
    vs[n1][n2] = vs[n2][n1] = 1

visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

def dfs(v) :
    visited_dfs[v] = 1 # 시작 정점 방문 표시
    print(v, end=" ") # 방문한 정점 출력 
    for i in range(1, n+1) : # 1부터 n까지 돌면서 현재 정점과 이어진 정점이 있는지 확인 
        # 현재 정점과 이어졌으면서 방문한 적 없는 정점이면 
        if vs[v][i] == 1 and visited_dfs[i] == 0 :
            dfs(i) # 또다시 dfs로 구역 넓히기 

def bfs(v) :
    queue = [v] # 시작 정점 큐에 넣고 방문 표시
    visited_bfs[v] = 1 
    while queue : 
        x = queue.pop(0) # 현재 방문한 정점 출력 
        print(x, end=" ")
        for i in range(1, n+1) : # 1부터 n까지 돌면서 현재 정점과 이어진 정점 확인 
            # 현재 정점과 이어져있고 방문한 적이 없다면 
            if vs[x][i] == 1 and visited_bfs[i] == 0 :
                visited_bfs[i] = 1 # i로 이동하면서 방문 표시
                queue.append(i) # 큐에 이어진 정점 집어넣기 

dfs(v)
print()
bfs(v)
