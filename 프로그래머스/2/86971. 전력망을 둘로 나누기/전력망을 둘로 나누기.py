from collections import deque 

def bfs(v, graph, visited) :
    queue = deque([v])
    visited[v] = 1
    cnt = 1 # 처음 bfs에 진입했을 때 카운트 
    while queue : 
        w = queue.popleft()
        for i in range(len(graph)) : 
            if visited[i] == 0 and graph[w][i] == 1 : # i번과 w번이 연결되어 있고 현재 i번을 방문한 적 없을 때
                queue.append(i)
                visited[i] = 1
                cnt += 1 # 이어져있는 송전탑의 개수 +1
    return cnt
            
    
def solution(n, wires):
    answer = n
    graph = [[0]*(n+1) for _ in range(n+1)] # 송전탑 연결 그래프 
    
    # 그래프에 송전탑 연결 표시 
    for wire in wires :
        w1, w2 = wire # 송전탑1, 송전탑2
        graph[w1][w2] = graph[w2][w1] = 1 # 송전탑1과 송전탑2가 연결되어 있음을 의미 
    
    for wire in wires :
        w1, w2 = wire # 송전탑1, 송전탑2로 분리 
        visited = [0] * (n+1)
        graph[w1][w2] = graph[w2][w1] = 0 # 두 송전탑의 연결 끊기 
        w1_cnt = bfs(w1, graph, visited) # w1쪽 송전탑의 개수 구하기
        w2_cnt = bfs(w2, graph, visited) # w2쪽 송전탑의 개수 구하기
        graph[w1][w2] = graph[w2][w1] = 1 # 두 송전탑을 다시 연결하기
        answer = min(answer, abs(w1_cnt-w2_cnt)) # 두 전력망이 가진 송전탑의 개수의 차이가 가장 적은 값 구하기 
        
    return answer