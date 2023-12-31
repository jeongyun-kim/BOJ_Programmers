import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
# N : 정점, M : 간선
# 인접 정점은 내림차순 

# 1. 변수 정의 및 초기화
N, M, R = map(int, input().split())
visited = [0] * (N+1)
order = 1 # 순서
answer = [0] * (N+1)

# 2. 행렬
graph = [[]*(N+1) for _ in range(N+1)]
for i in range(M) :
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 3. 인접정점 내림차순으로
for i in range(1, N+1) :
    graph[i] = sorted(graph[i], reverse=True)

# 4. dfs
def dfs(R) :
    global graph, visited, order, answer
    visited[R] = 1
    answer[R] = order
    order += 1
    for i in graph[R] :
        if visited[i] == 0 :
            dfs(i)

# 5. dfs 호출
dfs(R)

# 6. 결과 출력
for j in range(1, N+1) :
    print(answer[j])
