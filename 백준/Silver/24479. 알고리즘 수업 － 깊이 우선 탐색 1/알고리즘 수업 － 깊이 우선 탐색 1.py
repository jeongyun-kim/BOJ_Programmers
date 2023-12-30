import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 1. 변수 정의
N, M, R = map(int, input().split())
answer = [0]*(N+1) # 순번이 들어갈 배열
order = 1 # 순번 
visited = [0]*(N+1) # 방문했는지 확인 

# 2. 행렬
graph = [[]*(N+1) for _ in range(N+1)]
for i in range(0, M) :
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 3. 행렬 각 행 오름차순으로 정렬
for i in range(1, N+1) :
    graph[i] = sorted(graph[i])

# 4. dfs 정의
def dfs(R) :
    global visited, graph, answer, order
    visited[R] = 1
    answer[R] = order
    order += 1
    for i in graph[R] :
        if visited[i] == 0 :
            dfs(i)

# 5. dfs 호출
dfs(R)

# 결과 출력
for j in range(1, N+1) :
    print(answer[j])

