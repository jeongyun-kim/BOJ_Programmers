import sys
sys.setrecursionlimit(10**7) # 재귀함수로 호출할 수 있는 제한을 늘려줌 
input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수 M
# 예제1 ) 1 - 2 - 5 / 3 - 4 - 6 > 2개

# 1. 입력 / 초기화 
MAX = 1000 + 10
N, M = map(int, input().split())
cnt = 0

# 2. 그래프 및 방문 노드 확인 배열 생성 
graph = [[0] * MAX for _ in range(MAX)]
visited = [0]*MAX

# 3. 연결 노드 체크
for i in range(M) :
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1
    
# 4. DFS 생성
def dfs(v) :
    global visited, graph
    visited[v] = 1
    for i in range(1, N+1) :
        if graph[v][i] == 1 and visited[i] == 0 :
            dfs(i)

# 5. dfs 호출
# 1부터 N까지의 노드를 돌며 해당 노드를 방문한 적이 없으면 dfs로 진입 -> 빠져나오면 count+1
for i in range(1, N+1) :
    if visited[i] == 0 :
        dfs(i)
        cnt += 1

# 6. 결과 출력
print(cnt)
