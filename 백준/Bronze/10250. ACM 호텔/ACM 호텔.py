# t : 테스트케이스의 개수
# h : 층수, w : 방 수, n : 손님의 순서
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t) :
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1
    if floor == 0 : # ex) 6층 호텔에 손님이 6번째로 방문했을 때 => floor : 0, room : 2 (실제 답은 601)
        room -= 1 # 룸 번호 하나 빼주고
        floor = h # 방의 층을 건물 높이로 고정 
    print(floor*100+room)