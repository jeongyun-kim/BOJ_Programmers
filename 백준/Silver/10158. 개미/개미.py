# 개미가 현 위치에서 다시 현 위치로 돌아오는데에는 2w, 2h만큼의 주기가 필요함
# 즉, 방향이 어떻든 해당 주기내의 위치에서 움직인다는 것을 알 수 있음
# 그러므로 주기동안 움직이는 x좌표, y좌표가 들어있는 리스트를 만들고 현재 위치에서 이동 시간을 더한 후 주기만큼 나누어줘 나온 나머지의 인덱스값이 최종 이동위치라고 생각할 수 있음
w, h = map(int,input().split())
x, y = map(int,input().split())
t = int(input())
ws, hs = [], []

# x 이동 좌표
for i in range(w) :
    ws.append(i)
for j in range(w, 0, -1) :
    ws.append(j)
# y 이동 좌표
for i in range(h):
    hs.append(i)
for j in range(h, 0, -1) :
    hs.append(j)
    
px = (x+t)%(2*w)
py = (y+t)%(2*h)

print(ws[px], hs[py])