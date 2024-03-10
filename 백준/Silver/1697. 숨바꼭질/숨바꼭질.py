# 수빈이가 걸을 때 1초 뒤 위치 : x-1 / x+1
# 수빈이가 순간이동한 후 위치 : 2*x
# 수빈이와 동생의 위치가 주어졌을 때
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초인지
n, k = map(int, input().split())
visited = [0] * 100001

def bfs() : 
    queue = [n] # 시작 위치 
    while queue :
        p = queue.pop(0) # 현재 위치 
        if p == k : # 수빈이 위치 = 동생 위치라면 
            print(visited[p])
            break
        # 수빈이가 이동할 수 있는 위치들(p-1, p+1, p*2)
        for position in (p-1, p+1, p*2) : 
            # 수빈이가 이동한 위치가 범위 내에 있고 해당 위치를 거쳐간적이 없다면
            if 0 <= position <= 100000 and visited[position] == 0 :
                # 이동한 위치까지의 시간 = 현재 이동위치까지의 시간 + 1초 
                visited[position] = visited[p] + 1
                # 이동 가능한 위치 추가 
                queue.append(position)
                
bfs()