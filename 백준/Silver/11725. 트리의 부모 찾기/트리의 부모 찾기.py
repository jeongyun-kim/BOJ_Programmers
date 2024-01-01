import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
# 각 노드의 부모 구하기
# 첫째줄에 노드의 개수 N
# 둘째줄~ : 연결된 두 정점

# 1. 변수 정의
N = int(input())
visited = [0]*(N+1)
answer = [0]*(N+1)

# 2. 행렬
graph = [[]*(N+1) for _ in range(N+1)]
for i in range(N-1) :
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 3. dfs
def dfs(V) :
    global graph, visited, answer
    visited[V] = 1
    for node in graph[V] :
        if visited[node] == 0 :
            answer[node] = V
            dfs(node)

# 4. dfs 호출
dfs(1)

# 5. 결과 출력
for i in range(2, N+1) :
    print(answer[i])