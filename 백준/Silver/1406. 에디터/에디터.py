# 영어 소문자만을 기록할 수 있고, 최대 600,000글자까지 입력 가능
# L : 커서를 왼쪽으로 옮김(커서가 문장의 맨 앞이면 무시)
# D : 커서를 오른쪽으로 옮김(커서가 문장의 맨 뒤면 무시)
# B : 커서 왼쪽의 문자를 삭제(커서가 문장의 맨 앞이면 무시)
# P : 공백 이후의 문자를 커서 왼쪽에 추가 
# 문자열이 주어지고 입력한 명령어를 수행한 문자열을 구하기 
# ! 명령어가 수행되기 전 커서는 문장의 맨 뒤에 위치 
import sys
input = sys.stdin.readline

left = list(input().rstrip())
order_cnt = int(input())
right = []

for i in range(order_cnt) :
    command_line = input().split()
    cmd = command_line[0]
    if cmd == "P" :
        left.append(command_line[1])
    elif cmd == "L" and left : 
        right.append(left.pop())
    elif cmd == "D" and right :
        left.append(right.pop())
    elif cmd =="B" and left:
        left.pop()

answer = left + right[::-1]
print(''.join(answer))