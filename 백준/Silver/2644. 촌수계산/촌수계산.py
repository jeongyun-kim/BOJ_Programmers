import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 변수 정의 및 초기화 
N = int(input())
start, end = map(int, input().split())
M = int(input())
answer = -1
MAX = 100 + 10
visited = [False] * MAX

# 행렬 정의 및 연결 관계 나타내기 
graph = [[False] * MAX for _ in range(MAX)]
for _ in range(M) :
    n1, n2 = map(int, input().split())
    graph[n1][n2] = True
    graph[n2][n1] = True

# dfs 정의
def dfs(V, cnt) :
    global visited, graph, end, answer
    visited[V] = True
    if V == end :
        answer = cnt
        return
    for i in range(1, N+1) :
        if not visited[i] and graph[V][i] :
            dfs(i, cnt+1)
   
# dfs 호출
dfs(start, 0)

# 결과 출력
print(answer)