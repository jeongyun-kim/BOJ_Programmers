# 10진법 수 N이 주어지면 이 수를 B진법으로 바꾸어 출력하기
# 10진법 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있음 => 10:A ~ 35:Z
# 아스키 코드 이용해보기 : 나머지가 10이상이라면 [10 + 아스키코드(A) 65 - 10]이 해당 알파벳의 아스키 코드 
import sys
input = sys.stdin.readline

answer = ""
n, b = map(int, input().split())

while n > 0 :
    n, r = divmod(n, b) 
    if r >= 10 : # 나머지가 10 이상이라면 
        answer += chr(r + 65 - 10)
    else :
        answer += str(r)

print(answer[-1::-1]) # 반대로 출력해주어야 맞음 
